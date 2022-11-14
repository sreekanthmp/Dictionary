from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from dict.models import Dictionary


class DictSerializer(ModelSerializer):


    class Meta:
        model = Dictionary
        fields = "__all__"
        
    
        
        
    