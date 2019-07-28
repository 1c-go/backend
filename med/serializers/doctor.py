from rest_framework import serializers

from ..models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField()

    class Meta:
        model = Doctor
        fields = '__all__'
