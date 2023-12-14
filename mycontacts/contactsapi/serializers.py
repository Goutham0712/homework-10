#Create the file contactsapi/serializers.py and add the code below:
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact 
        fields = ('first_name', 'last_name','email')