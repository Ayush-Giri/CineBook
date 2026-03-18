from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from movies.models import Movies
from movies.serializers import MovieSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.



class MovieViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


    @action(detail=True, methods=['patch'], permission_classes=[IsAdminUser])
    def deactivate(self, request, pk=None):
        # movie_instance = Movies.objects.get(id=pk)
        # serializer = self.get_serializer(movie_instance, data=request.data, context={"request": request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(
        #         status=status.HTTP_200_OK
        #     )
        # return Response(status=status.HTTP_400_BAD_REQUEST)
        movie_instance = self.get_object()
        movie_instance.is_active=False
        movie_instance.save()
        return Response(
            status=status.HTTP_200_OK
        )





class DeactivateMove(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, id):
        try:
            movie_instance = Movies.objects.get(id=id)
            serializer = MovieSerializer(movie_instance, data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        except Movies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


