from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

__all__ = ['CustomTokenObtainSerializer']


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField()

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        if self.user is None or not self.user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        return {}
    '''
    def validate(self, attrs):
        data = super().validate(attrs)
        data["full_name"] = self.user.full_name
        return data
