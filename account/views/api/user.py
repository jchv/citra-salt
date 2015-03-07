from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from account.models import User
from account.serializers.user import UserSerializer, CredentialsSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This endpoint enables creating, enumerating and manipulating user accounts.
    # Fields
      * `username`: Alphanumeric ID, max length 20. Must be unique.
      * `password`: _[write only]_ Account password. Unicode not recommended due to differences between platforms.
      * `email`: A valid e-mail address. Must be unique.
      * `display_name`: Display name; max length 48 characters. Must be unique.
      * `location`: _[optional]_ A phrase representing user's location.
      * `birth_date`: _[optional]_ The user's birthdate (in ISO 8601 format.)
      * `gender`: _[optional]_ A phrase representing user's gender.
      * `pronouns`: Pronouns to use for user. Possible choices:
          * `m`: Male pronouns (he, him, his)
          * `f`: Female pronouns (she, her, hers)
          * `n`: Neutral pronouns (they, them, their, theirs)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(viewsets.GenericViewSet):
    """
    This endpoint handles session cookie based authentication.
    # Fields
      * `username`: A valid username.
      * `password`: A password.
    """
    serializer_class = CredentialsSerializer

    def login(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=200, data=UserSerializer(user, context={'request': request}).data)
            else:
                raise ValidationError('User account inactive.')
        else:
            raise ValidationError('Bad username or password.')


class LogoutView:
    @staticmethod
    def logout(request):
        """
        Logs out of the current cookie-based session.
        """
        logout(request)
        return Response(status=200)


List = UserViewSet.as_view({'get': 'list', 'post': 'create'}, suffix='List')
Detail = UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}, suffix='Detail')
Login = LoginView.as_view({'post': 'login'})
Logout = api_view(['POST'])(LogoutView.logout)
