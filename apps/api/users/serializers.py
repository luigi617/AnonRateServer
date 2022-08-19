from rest_framework import serializers
from apps.user.models import User



class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'username']
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "last_name", "first_name", "avatar_thumbnail"]

class UserListSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["id", 'username', "last_name", "first_name", "avatar_thumbnail", "rate"]

    def get_rate(self, instance):
        if instance.rating.exists():
            rating_list = instance.rating.values_list("rating", flat = True)
            mean = sum(rating_list)/len(rating_list)
            return f"{mean/10}/10"
        return "no rating"

# from phonenumber_field.serializerfields import PhoneNumberField
# from config.phoneValidation.backends.backends import get_sms_backend

# class PhoneSerializer(serializers.Serializer):
#     phone_number = PhoneNumberField()


# class SMSVerificationSerializer(serializers.Serializer):
#     phone_number = PhoneNumberField(required=True)
#     session_token = serializers.CharField(required=True)
#     security_code = serializers.CharField(required=True)

#     def validate(self, attrs):
#         attrs = super().validate(attrs)
#         phone_number = attrs.get("phone_number", None)
#         security_code, session_token = (
#             attrs.get("security_code", None),
#             attrs.get("session_token", None),
#         )
#         backend = get_sms_backend(phone_number=phone_number)
#         verification, token_validatation = backend.validate_security_code(
#             security_code=security_code,
#             phone_number=phone_number,
#             session_token=session_token,
#         )

#         if verification is None:
#             raise serializers.ValidationError(_("Security code is not valid"))
#         elif token_validatation == backend.SESSION_TOKEN_INVALID:
#             raise serializers.ValidationError(_("Session Token mis-match"))
#         elif token_validatation == backend.SECURITY_CODE_EXPIRED:
#             raise serializers.ValidationError(_("Security code has expired"))
#         elif token_validatation == backend.SECURITY_CODE_VERIFIED:
#             raise serializers.ValidationError(_("Security code is already verified"))

#         return attrs