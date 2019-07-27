from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

__all__ = ['CustomTokenObtainSerializer']


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["full_name"] = self.user.full_name
        return data
