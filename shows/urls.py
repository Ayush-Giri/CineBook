from rest_framework.routers import DefaultRouter
from shows.views import ShowViewSet
from django.urls import path,include

router = DefaultRouter()
router.register(r"shows", ShowViewSet)


urlpatterns = [
    path("", include(router.urls))
]