from dog.serializers import DogSerializer
from dog.models import Dog
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

#combine get and post request together
@api_view(['GET','POST'])
def dogs(request):
	if request.method == 'GET':
		dog = Dog.objects.all()
		serializer = DogSerializer(dog, many=True)
		return Response({"data":serializer.data},status.HTTP_200_OK)

	elif request.method == 'POST':
		serializer = DogSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"message":"The dog has been created successfully",
                            "data" : serializer.data

            },status.HTTP_201_CREATED)
        
		# return Response( {"success": False, "status_code": 1,"errors": serializer.errors,
        #                      "status_message": "Cannot save dog details",
        #                      "message": "cannot save dog details", "data": None
        #                      },)
