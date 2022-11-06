from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from content.serializers import ContentSerializer, RateSerializer
from content.models import Content, Rate
from django.db.models import Avg


class ContentViewSet(
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    GenericAPIView
):
    model = Content
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(avg_rate=Avg("rate"))
        return qs


class RateViewSet(
    CreateAPIView,
    GenericAPIView
):
    lookup_field = "id"
    model = Rate
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def create(self, request, *args, **kwargs):
        rate = self.request.data.get('rate', None)
        content = self.request.data.get('content', None)
        user = self.request.data.get('user', None)

        if not rate:
            return Response({"message": "Rate field is mandatory."}, status=400)
        if not content:
            return Response({"message": "Content field is mandatory."}, status=400)
        if not user:
            return Response({"message": "user field is mandatory."}, status=400)

        if not Content.objects.filter(id=content).exists():
            return Response({"message": "Content with this id, not found."}, status=404)

        return super().create(request, *args, **kwargs)
