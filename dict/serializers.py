from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from dict.models import Dictionary
from dict.models import Dict


class Dict2Serializer(ModelSerializer):
    
    class Meta:
        model = Dict
        fields = "__all__"


class DictSerializer(ModelSerializer):



    class Meta:
        model = Dictionary
        fields = "__all__"
        
    
        
        
    