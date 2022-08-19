
from apps.api.paginations import StandardResultsSetPagination
from apps.api.users.serializers import UserCreationSerializer, UserListSerializer, UserProfileSerializer
from apps.user.models import User
from rest_framework import views, generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import response
# from apps.api.users.serializers import PhoneSerializer, SMSVerificationSerializer
# from config.phoneValidation.services import send_security_code_and_generate_session_token



# class VerificationViewSet(viewsets.ViewSet):
#     @action(
#         detail=False,
#         methods=["POST"],
#         permission_classes=[AllowAny],
#         serializer_class=PhoneSerializer,
#     )
#     def register(self, request):
#         print(request.data)
#         serializer = PhoneSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         session_token = send_security_code_and_generate_session_token(
#             str(serializer.validated_data["phone_number"])
#         )
#         return response.Response({"session_token": session_token})

#     @action(
#         detail=False,
#         methods=["POST"],
#         permission_classes=[AllowAny],
#         serializer_class=SMSVerificationSerializer,
#     )
#     def verify(self, request):
#         serializer = SMSVerificationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return response.Response({"message": "Security code is valid."})
class UserLoggedInVerificationViewSet(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        data = {
            "username": username,
            "available": True,
            "message": "ok",
        }
        if User.objects.filter(username = username).exists():
            data["available"] = False
            data["message"] = "Username is already used by others"
        return response.Response(data)
class UsernameVerificationViewSet(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        data = {
            "username": username,
            "available": True,
            "message": "ok",
        }
        if User.objects.filter(username = username).exists():
            data["available"] = False
            data["message"] = "Username is already used by others"
        return response.Response(data)

class UserCreationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.create_user(username, None, password)
        return response.Response(UserCreationSerializer(user).data)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    pagination_class = StandardResultsSetPagination

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj


    

class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def update(self, request, *args, **kwargs):
        last_name = request.data.get("last_name")
        first_name = request.data.get("first_name")
        avatar = request.FILES.get("avatar")
        instance = self.get_object()
        serializer = UserProfileSerializer(instance, data={
            "last_name": last_name,
            "first_name": first_name,
            "avatar_thumbnail": avatar,
        }, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return response.Response(serializer.data)



   