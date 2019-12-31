#from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Values

from .serializers import ValuesSerializer
from rest_framework import status

@api_view(['GET','POST'])
def key_val(request):

    if request.method == 'GET':
        obj=Values.objects.all()
        serializer=ValuesSerializer(obj , many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer=ValuesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

@api_view(['GET','PATCH'])
def value_detail(request,pk):
    try:
        obj= Values.objects.get(id=pk)
    except Values.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer= ValuesSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer= ValuesSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    #serializer= ValuesSerializer(obj)
    #return Response(serializer.data)
