from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from med.models import Patient
from ..models import CustomUser

__all__ = ['RegistrationSerializer']


class RegistrationSerializer(serializers.ModelSerializer):
    _validator = UniqueValidator(queryset=CustomUser.objects.all())
    email = serializers.EmailField(validators=[_validator], required=False)
    username = serializers.CharField(validators=[_validator])

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'password')

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        patient = Patient.objects.create(user=user)
        return user
