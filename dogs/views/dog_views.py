from django.shortcuts import render, get_object_or_404 
from .serializers import DogSerializer
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response 

from ..models import Dog 

# Create your views here.

# index all 
# localhost:3000/hospital/  get  post (for a single doctor)
class DogsView(APIView):
    """View class for dogs/ for viewing all and creating"""
    def get(self, request):
        dogs = Dog.objects.all()
        # take a model, pass it into a serializer and transform the query set so we can utilize it.
        serializer = DogSerializer(dogs, many=True)
        return Response({'dogs': serializer.data})

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # tell it what to return in parens
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# localhost:3000/dog/:id   get  delete  update (for a single dog)
class DogDetailView(APIView):
    """View class for dogs/:pk for viewing a single dog, updating a single dog, or removing a single dog"""
    def get(self, request, pk):
    # this tells it where to look (Dog) and what to find (pk)
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog)
        # just one book b/c it's just representing one book here
        return Response({'dog': serializer.data})

    # updating a single dog
    def patch(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog,
        data=request.data)
        if serializer.is_valid():
            serializer.save()
            # tell it what to return in parens
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single dog
    def delete(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)