from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models import CustomUser
from med.models import Hospital

__all__ = ['RegistrationSerializer']


class RegistrationSerializer(serializers.ModelSerializer):
    _validator = UniqueValidator(queryset=CustomUser.objects.all())
    hospital = serializers.PrimaryKeyRelatedField(queryset=Hospital.objects)
    email = serializers.EmailField(validators=[_validator])
    username = serializers.CharField(validators=[_validator])

    class Meta:
        model = CustomUser
        fields = ('full_name', 'email', 'password', 'hospital')

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'],
                                              validated_data['password'])
        return user
