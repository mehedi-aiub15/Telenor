from django.db import models

# Create your models here.

class Values(models.Model):
    key=models.CharField(max_length=20)
    value=models.TextField(blank='False',default='')

    def __str__(self):
        return self.key
