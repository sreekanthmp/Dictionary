from django.shortcuts import render
import json
from rest_framework.viewsets import ModelViewSet
from dict import serializers
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from dict.serializers import DictSerializer
from dict.models import Dictionary
from rest_framework.permissions import IsAuthenticated

class PostViewSet(ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictSerializer
     

    def get_search(self, request, *args, **kwargs):
        user_list = Dictionary.objects.all()
        query_set = user_list.filter(label__startswith=request.query_params.get('search'))
        serializer = DictSerializer(query_set, many=True)
        if(user_list.filter(label=request.query_params.get('search')).exists()):
            exactMatchObject = get_object_or_404(Dictionary,label=request.query_params.get('search'))
            
            print(exactMatchObject)
            exactMatchObject.search_count = exactMatchObject.search_count + 1
            exactMatchObject.save()
        return Response(serializer.data)  
    
    