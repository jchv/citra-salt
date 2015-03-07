from django.db import transaction
from django.db.models import F
from rest_framework import serializers
import reversion
from account.models import User

from blog.models import Post, Authorship, Tag


class PostAuthorshipMixin(object):
    """
    This mixin handles writing authorship information for blog posts.
    """

    def get_request_and_user(self):
        request, user = None, None
        if 'request' in self.context:
            request = self.context['request']
            if request.user and request.user.is_authenticated():
                user = request.user
        return request, user

    def create(self, validated_data):
        request, user = self.get_request_and_user()

        with transaction.atomic(), reversion.create_revision():
            obj = super().create(validated_data)
            if user is not None:
                reversion.set_user(user)
            if 'comment' in self.context:
                reversion.set_comment(self.context['comment'])

        if user is not None:
            Authorship.objects.create(
                user=user,
                post=obj,
                char_count=len(validated_data['content']),
                edit_count=1,
                role=Authorship.ROLE_WRITER
            )

        return obj

    def update(self, instance, validated_data):
        request, user = self.get_request_and_user()

        # TODO: use a diff to get a -real- count here.
        change_count = abs(len(instance.content) - len(validated_data['content']))

        with transaction.atomic(), reversion.create_revision():
            obj = super().update(instance, validated_data)
            if user is not None:
                reversion.set_user(user)
            if 'comment' in self.context:
                reversion.set_comment(self.context['comment'])

        if user is not None:
            # Wish we could do this atomically in one SQL statement.
            with transaction.atomic():
                rows = Authorship.objects.filter(post=obj, user=user)\
                                         .update(edit_count=F('edit_count') + 1,
                                                 char_count=F('char_count') + change_count)
                if rows < 1:
                    Authorship.objects.create(
                        user=user,
                        post=obj,
                        char_count=change_count,
                        edit_count=1,
                        role=Authorship.ROLE_EDITOR
                    )

        return obj


class PostListSerializer(PostAuthorshipMixin, serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='title', many=True, queryset=Tag.objects.all())
    slug = serializers.CharField(required=False, allow_blank=True)
    authors = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)
    content = serializers.CharField(source='content_brief')

    class Meta:
        model = Post
        fields = ('id', 'authors', 'tags', 'title', 'slug', 'content',
                  'image', 'is_published', 'url',
                  'date_published', 'date_modified')
        read_only_fields = ('date_modified', 'date_published')
        extra_kwargs = {
            'url': {'view_name': 'api:blog:post-detail'}
        }

    def create(self, validated_data):
        validated_data['content'] = validated_data.pop('content_brief')
        return super().create(validated_data)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'display_name', 'personal_name', 'location', 'birth_date',
                  'gender', 'pronouns', 'is_staff', 'is_active', 'date_joined')
        extra_kwargs = {
            'url': {'view_name': 'api:account:user-detail'}
        }


class AuthorshipSerializer(serializers.ModelSerializer):
    user = AuthorSerializer()

    class Meta:
        model = Authorship
        fields = ('user', 'char_count', 'edit_count', 'role')


class PostSerializer(PostAuthorshipMixin, serializers.HyperlinkedModelSerializer):
    authors = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)
    authors_detailed = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(slug_field='title', many=True, queryset=Tag.objects.all())
    slug = serializers.SlugField(max_length=128, required=False, allow_blank=True)
    authors_url = serializers.HyperlinkedIdentityField(view_name='api:blog:author-list')

    class Meta:
        model = Post
        fields = ('id', 'authors', 'authors_detailed', 'tags', 'title', 'title_seo',
                  'slug', 'content', 'image', 'is_published', 'url', 'authors_url',
                  'date_created', 'date_modified', 'date_published')
        read_only_fields = ('date_created', 'date_modified', 'date_published')
        extra_kwargs = {
            'title_seo': {'required': False},
            'url': {'view_name': 'api:blog:post-detail'}
        }

    def get_authors_detailed(self, obj):
        return AuthorshipSerializer(Authorship.objects.filter(post=obj), many=True).data
