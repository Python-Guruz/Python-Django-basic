from django.db.models import fields
from rest_framework import serializers
from dog.models import Dog

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ("id","name","age")

    def save(self,*args,**kwargs):
        dog = Dog(
            name = self.validated_data["name"],
            age = self.validated_data["age"]
        )
        dog.save()
        return dog