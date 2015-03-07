from collections import OrderedDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def blog_root(request, format=None):
    """
    This is a list of all of the blog endpoints.
    """
    return Response(OrderedDict([
        ('posts', reverse('api:blog:post-list', request=request, format=format)),
        ('tags', reverse('api:blog:tag-list', request=request, format=format)),
    ]))
