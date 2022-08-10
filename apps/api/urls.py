
from apps.api.users.urls import users_urlpatterns
from apps.api.home.urls import home_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns(
    home_urlpatterns
)