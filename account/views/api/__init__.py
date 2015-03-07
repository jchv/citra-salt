from collections import OrderedDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def account_root(request, format=None):
    """
    This is a list of all of the account endpoints.
    """
    return Response(OrderedDict([
        ('login', reverse('api:account:login', request=request, format=format)),
        ('logout', reverse('api:account:logout', request=request, format=format)),
        ('users', reverse('api:account:user-list', request=request, format=format))
    ]))
