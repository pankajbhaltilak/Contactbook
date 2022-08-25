from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerializer(ModelSerializer):

    class Meta:
        model=Contact

        fields=['LastName' , 'Email' ,'ContactNumber']