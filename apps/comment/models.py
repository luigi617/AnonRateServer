from django.db import models

from ..user.models import User


class Comment(models.Model):
    """
    Not used for now.
    The comment is anonymous, therefore we do not store the sender information
    """
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(User, related_name="comments", on_delete=models.PROTECT)