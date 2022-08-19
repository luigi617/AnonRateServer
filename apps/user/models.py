import os
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill



def avatar_location(instance, filename):
    folder_name = f'users/avatars/'
    return os.path.join(folder_name, filename)
class User(AbstractUser):
    # phone = PhoneNumberField(unique=True, null=True)
    avatar_thumbnail = ProcessedImageField(upload_to=avatar_location,
                                           processors=[ResizeToFill(100, 100)],
                                           format='JPEG',
                                           options={'quality': 100},
                                           null=True,
                                           blank=True,
                                           )

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)

class Label(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User, related_name="labels")
    
# class SMSVerification(models.Model):
#     security_code = models.CharField(_("Security Code"), max_length=120)
#     phone_number = PhoneNumberField(_("Phone Number"))
#     session_token = models.CharField(_("Device Session Token"), max_length=500)
#     is_verified = models.BooleanField(_("Security Code Verified"), default=False)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     modified_at = models.DateTimeField(auto_now=True, editable=False)

#     class Meta:
#         db_table = "sms_verification"
#         verbose_name = _("SMS Verification")
#         verbose_name_plural = _("SMS Verifications")
#         ordering = ("-modified_at",)
#         unique_together = ("security_code", "phone_number", "session_token")

#     def __str__(self):
        # return "{}: {}".format(str(self.phone_number), self.security_code)