from django.db import models



class Dictionary(models.Model):
    label=models.CharField(max_length=200)
    description=models.TextField()
    
class Dict(models.Model):
    search_count=models.IntegerField(default=0)
    dict_id=models.IntegerField()
