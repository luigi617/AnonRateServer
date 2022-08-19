
from apps.api.paginations import StandardResultsSetPagination
from apps.api.rating.serializers import RatingListCreateSerializer
from apps.rating.models import Rating
from rest_framework import views, generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import response


class RatingListCreateView(generics.ListCreateAPIView):
    serializer_class = RatingListCreateSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        return Rating.objects.filter(recipient = user).order_by("-date_created")

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserListSerializer
#     pagination_class = StandardResultsSetPagination


    




   