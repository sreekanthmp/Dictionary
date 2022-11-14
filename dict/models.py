from django.db import models

    
class Dictionary(models.Model):
    label=models.CharField(max_length=200)
    description=models.TextField()
    search_count=models.IntegerField(default=0)



    