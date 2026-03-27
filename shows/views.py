from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from shows.models import Shows
from shows.serializers import ShowSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ShowViewSet(ModelViewSet):
    queryset = Shows.objects.all()
    serializer_class = ShowSerializer

    @action(detail=True, methods=["patch"])
    def deactivate_show(self, request, pk=None):
        show_instance = self.get_object()
        show_instance.is_active=False
        show_instance.save()
        return Response(
            {"message": "show deactived successsfully"},
            status=status.HTTP_200_OK
        )






