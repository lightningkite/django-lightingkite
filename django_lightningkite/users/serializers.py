from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions, serializers

UserModel = get_user_model()
EMAIL_REQUIRED = True
UNIQUE_EMAIL = True


def email_exists(email):
    return UserModel.objects.filter(email=email).exists()


def clean_email(email):
    return email


def clean_password(password, user=None):
    min_length = 8
    if min_length and len(password) < min_length:
        raise forms.ValidationError(_("Password must be a minimum of {0} "
                                        "characters.").format(min_length))
    validate_password(password, user)
    return password


if 'allauth' in settings.INSTALLED_APPS:
    from allauth.account import app_settings as allauth_settings
    from allauth.utils import email_address_exists
    from allauth.account.adapter import get_adapter
    EMAIL_REQUIRED = allauth_settings.EMAIL_REQUIRED
    UNIQUE_EMAIL = allauth_settings.UNIQUE_EMAIL
    email_exists = email_address_exists
    clean_email = get_adapter.clean_email
    clean_password = get_adapter.clean_password


class EmailUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = self._validate_email(email, password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    raise serializers.ValidationError(_('E-mail is not verified.'))

        attrs['user'] = user
        return attrs


class EmailUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'date_joined',
        )
        read_only_fields = ('id', 'email', 'date_joined')


class EmailRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=EMAIL_REQUIRED)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = clean_email(email)
        if UNIQUE_EMAIL:
            if email and email_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address.")
                )
        return email

    def validate_password1(self, password):
        return clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def create(self, validated_data):
        User = get_user_model()
        password = validated_data.pop('password1', None)
        user = User(email=validated_data.get('email', ''))
        user.set_password(password)
        user.save()
        return user

    def save(self, request=None):
        return super(EmailRegisterSerializer, self).save()
