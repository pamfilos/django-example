from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from groups.users.api.views import UserViewSet
from groups.groups.api.views import GroupViewSet
from groups.mini_apps.api.views import MiniAppsViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
router.register("miniApps", MiniAppsViewSet)


app_name = "api"
urlpatterns = router.urls
