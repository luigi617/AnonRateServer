from django.db import models

from ..user.models import User

# Create your models here.
class Comment(models.Model):
    """
    The comment is anonymous, therefore we do not store the sender information
    """
    content = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(User, related_name="comments", on_delete=models.PROTECT)