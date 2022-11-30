from django.shortcuts import render, get_object_or_404 
from .serializers import CatSerializer
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response 

from .models import Cat 

# Create your views here.

# index all 
# localhost:3000/hospital/  get  post (for a single doctor)
class CatsView(APIView):
    """View class for cats/ for viewing all and creating"""
    def get(self, request):
        cats = Cat.objects.all()
        # take a model, pass it into a serializer and transform the query set so we can utilize it.
        serializer = CatSerializer(cats, many=True)
        return Response({'cats': serializer.data})

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # tell it what to return in parens
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# localhost:3000/hospital/:id   get  delete  update (for a single doctor)
class CatDetailView(APIView):
    """View class for cats/:pk for viewing a single cat, updating a single cat, or removing a single cat"""
    def get(self, request, pk):
    # this tells it where to look (Book) and what to find (pk)
        cat = get_object_or_404(Cat, pk=pk)
        serializer = CatSerializer(cat)
        # just one book b/c it's just representing one book here
        return Response({'cat': serializer.data})

    # updating a single cat
    def patch(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        serializer = CatSerializer(cat,
        data=request.data)
        if serializer.is_valid():
            serializer.save()
            # tell it what to return in parens
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single doctor
    def delete(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)