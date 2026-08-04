from django.contrib.auth.backends import ModelBackend
from .models import User
from django.db.models import Q

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username=kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return None
        try:
            user=User.objects.get(Q(email=username) | Q(username=username))
        except User.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None