from config.dog.serializers import DogSerializer
from config.dog.models import Dog
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

#combine get and post request together
api_view(["GET","POST"])
def dogs(request):
    if request.method == "GET":
        dogs = Dog.objects.all()        
        serializer = DogSerializer(dogs,many=True)
        return Response(serializer.data)
