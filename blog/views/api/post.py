from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from blog.models import Post, Authorship
from blog.serializers.post import PostSerializer, PostListSerializer, AuthorshipSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    This endpoint allows you to list, retrieve, and manipulate blog posts.
    # Fields
      * `authors`: _[read only]_ A list of authors who have worked on this document.
      * `tags`: A list of tags associated with this document.
      * `title`: The title of the blog post.
      * `slug`: _[optional]_ The slug for the blog post.
      * `content`: The blog post content.
      * `image`: _[optional]_ An image to associate with the blog post.
      * `is_published`: Whether or not the blog should be published.
         _Setting this to `true` will cause the article to be published._
      * `date_published`: _[read only]_ The date the article was published in ISO 8601 format,
         or null if it has not been.
      * `date_modified`: _[read only]_ The date the article was last modified in ISO 8601 format.
    """
    queryset = Post.objects.all().prefetch_related('authors', 'tags')
    serializer_class = PostSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorshipSerializer
    lookup_url_kwarg = 'user_id'
    lookup_field = 'user'

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return Authorship.objects.filter(post=post)

List = PostViewSet.as_view({'get': 'list', 'post': 'create'}, suffix='List', serializer_class=PostListSerializer)
Detail = PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}, suffix='Detail')
AuthorList = AuthorViewSet.as_view({'get': 'list', 'post': 'create'}, suffix='List')
AuthorDetail = AuthorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}, suffix='Detail')
