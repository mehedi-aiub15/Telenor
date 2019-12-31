from rest_framework import serializers
from .models import Values

class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Values
        fields=('id','key','value')
