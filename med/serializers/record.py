from rest_framework import serializers

from ..models import Record


class RecordSerializer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField()
    patient = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    hospital = serializers.SerializerMethodField()
    specialization = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = '__all__'

    def get_patient(self, obj: Record):
        return {'id': obj.patient.id,
                'full_name': obj.patient.user.full_name}

    def get_doctor(self, obj: Record):
        return {'id': obj.doctor.id,
                'full_name': obj.doctor.full_name}

    def get_hospital(self, obj: Record):
        return {'id': obj.hospital.id,
                'name': obj.hospital.name}

    def get_specialization(self, obj: Record):
        return {'id': obj.specialization_id,
                'name': obj.specialization.name}

    def get_status(self, obj: Record):
        return obj.get_status_display()


class RecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('doctor', 'recording_at', 'specialization', 'title', 'hospital', 'description')
