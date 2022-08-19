from rest_framework import serializers
from apps.post.models import Post, PostImage
from apps.api.users.serializers import UserProfileSerializer


class PostImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["id", "file", "post"]

class PostListSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    images = PostImageListSerializer(many=True, read_only = True)
    class Meta:
        model = Post
        fields = ["id", 'user', "content", "date_created", "images"]

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", 'user', "content", "date_created"]




