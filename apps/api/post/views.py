
from apps.api.paginations import StandardResultsSetPagination
from apps.api.post.serializers import PostCreateSerializer, PostImageListSerializer, PostListSerializer
from apps.post.models import Post
from rest_framework import views, generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import response


class PostListCreationView(generics.ListCreateAPIView):
    serializer_class = PostListSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        userId = self.request.query_params.get("userId")
        print(userId, "*"*13)
        filter_data = {}
        if userId:
            filter_data["user"] = userId
        return Post.objects.filter(**filter_data).order_by("-date_created")

    def create(self, request, *args, **kwargs):
        content = request.data.get("content", "")
        images = request.FILES.getlist("post_images")
        post_serializer = PostCreateSerializer(data = {
            "content": content,
            "user": request.user.id,
        })
        if post_serializer.is_valid():
            post_serializer.save()
        
            post_id = post_serializer.data.get("id")
            for img in images:
                post_image_serializer = PostImageListSerializer(data = {
                    "post": post_id,
                    "file": img
                })
                if post_image_serializer.is_valid():
                    post_image_serializer.save()
        else:
            print(post_serializer.errors)
        return response.Response(post_serializer.data)






   