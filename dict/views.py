from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json

from dict.serializers import DictSerializer
from dict.serializers import Dict2Serializer
from dict.models import Dictionary
from dict.models import Dict


class PostViewSet(ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictSerializer
     

    def get_search(self, request, *args, **kwargs):
        dictionary_list = Dictionary.objects.all()
        dict_list = Dict.objects.all()
        query_set = dictionary_list.filter(label__startswith=request.query_params.get('search'))     
        serializer = DictSerializer(query_set, many=True)
        data_payload = {}
        data_payload = json.dumps(serializer.data)
        data_payload  = json.loads(data_payload)
        data_payload = data_payload[0]
        if(dictionary_list.filter(label=request.query_params.get('search')).exists()):
            dictionaryObject = get_object_or_404(Dictionary,label=request.query_params.get('search'))
            if(dict_list.filter(dict_id=dictionaryObject.id).exists()):
                dictObject=get_object_or_404(Dict,dict_id=dictionaryObject.id)
                dictObject.search_count=dictObject.search_count+1
                data_payload["search_count"]=dictObject.search_count
                dictObject.save()
            else:
                 dict_data_payload = {}
                 dict_data_payload["dict_id"] = dictionaryObject.id
                 dict_data_payload["search_count"]= 1
                 data_payload["search_count"]= 1
                 dictSerializer = Dict2Serializer(data=dict_data_payload)
                 if dictSerializer.is_valid():
                    dictSerializer.save()
        return Response(data_payload)  
    
     
    
    