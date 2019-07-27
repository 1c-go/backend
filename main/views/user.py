from django.core.exceptions import ValidationError
from rest_framework import permissions
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from main.serializers.user import RegistrationSerializer
from ..serializers.token import CustomTokenObtainSerializer
from ..models import CustomUser

__all__ = ['CustomTokenObtainView']


class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


'''
вход:
по почте
по логину
'''


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = RegistrationSerializer(request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except DRFValidationError as e:
            return Response({'success': False, 'errors': e.detail})
        except ValidationError as e:
            return Response({'success': False, 'errors': e.error_list})

        return Response({'success': True})
