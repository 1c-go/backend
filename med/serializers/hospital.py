from rest_framework import serializers

from ..models import Hospital


class HospitalSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField()

    class Meta:
        model = Hospital
        fields = '__all__'
