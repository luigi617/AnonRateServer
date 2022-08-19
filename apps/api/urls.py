
from apps.api.users.urls import users_urlpatterns
from apps.api.post.urls import posts_urlpatterns
from apps.api.rating.urls import rating_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns(
    users_urlpatterns + posts_urlpatterns + rating_urlpatterns
)