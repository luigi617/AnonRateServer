from django.db import models

from ..user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Rating(models.Model):
    """
    The rating is anonymous, therefore we do not store the sender information
    """
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100),
    ], null=True)
    recipient = models.ForeignKey(User, related_name="rating", on_delete=models.PROTECT)