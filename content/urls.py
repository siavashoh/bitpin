from django.urls import path
from content.views import ContentViewSet, RateViewSet
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register('', ContentViewSet, basename="content")
# router.register('rate/', RateViewSet, basename="rate")

urlpatterns = [
    path(
        "",
        ContentViewSet.as_view(),
    ),
    path(
        "rate/",
        RateViewSet.as_view(),
    )
]