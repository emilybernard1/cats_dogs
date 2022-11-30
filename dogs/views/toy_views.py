from django.shortcuts import render, get_object_or_404 
from .serializers import ToySerializer
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response 

from ..models import Toy 

# Create your views here.

# index all 
# localhost:3000/hospital/  get  post (for a single toy)
class ToysView(APIView):
    """View class for toys/ for viewing all and creating"""
    def get(self, request):
        toys = Toy.objects.all()
        # take a model, pass it into a serializer and transform the query set so we can utilize it.
        serializer = ToySerializer(toys, many=True)
        return Response({'toys': serializer.data})

    def post(self, request):
        serializer = ToySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # tell it what to return in parens
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# localhost:3000/toy/:id   get  delete  update (for a single toy)
class ToyDetailView(APIView):
    """View class for toys/:pk for viewing a single toy, updating a single toy, or removing a single toy"""
    def get(self, request, pk):
    # this tells it where to look (Toy) and what to find (pk)
        toy = get_object_or_404(Toy, pk=pk)
        serializer = ToySerializer(toy)
        # just one book b/c it's just representing one book here
        return Response({'toy': serializer.data})

    # updating a single toy
    def patch(self, request, pk):
        toy = get_object_or_404(Toy, pk=pk)
        serializer = ToySerializer(toy,
        data=request.data)
        if serializer.is_valid():
            serializer.save()
            # tell it what to return in parens
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single toy
    def delete(self, request, pk):
        toy = get_object_or_404(Toy, pk=pk)
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)