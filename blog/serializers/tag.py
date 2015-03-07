from rest_framework import serializers
from blog.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.SlugField(max_length=64)
    description = serializers.CharField(allow_blank=True)

    class Meta:
        model = Tag
        fields = ('title', 'description', 'url')
        extra_kwargs = {
            'url': {'view_name': 'api:blog:tag-detail', 'lookup_field': 'title'}
        }
