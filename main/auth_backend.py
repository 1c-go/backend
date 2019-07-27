from django.contrib.auth.backends import ModelBackend

from main.models import CustomUser

__all__ = ['CustomAuthBackend']


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            CustomUser().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
