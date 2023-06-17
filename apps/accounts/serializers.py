from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

Worker = get_user_model()


class TokenObtainPairSerializer(serializers.Serializer):
    username_field = Worker.USERNAME_FIELD

    default_error_messages = {
        'no_active_account': 'No active account found with the given credentials'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = serializers.CharField(
            style={'input_type': 'password'},
            trim_whitespace=False
        )

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }

        user = Worker.objects.filter(**{self.username_field: authenticate_kwargs[self.username_field]}).first()

        if user and user.is_active:
            if not user.check_password(authenticate_kwargs['password']):
                raise serializers.ValidationError(
                    self.default_error_messages['no_active_account']
                )
        else:
            raise serializers.ValidationError(
                self.default_error_messages['no_active_account']
            )

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }