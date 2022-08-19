from django.db import models

from ..user.models import User
import os

# Create your models here.
class Post(models.Model):
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)

def post_image_location(instance, filename):
    folder_name = f'posts/images/'
    return os.path.join(folder_name, filename)
class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)
    file = models.FileField(upload_to=post_image_location)
