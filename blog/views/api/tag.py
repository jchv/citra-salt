from rest_framework import viewsets
from blog.models import Tag
from blog.serializers.tag import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    This endpoint allows you to list, retrieve, and manipulate tags.
    # Fields
      * `title`: The title of the tag.
      * `description`: A description of the tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'title'
    lookup_url_kwarg = 'title'


List = TagViewSet.as_view({'get': 'list', 'post': 'create'}, suffix='List')
Detail = TagViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}, suffix='Detail')
