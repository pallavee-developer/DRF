from django.shortcuts import render
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def Homeview(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateView(request):
    serializers = TaskSerializer(data= request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def UpdateView(request,pk):
    task =Task.objects.get(pk=pk)
    serializers = TaskSerializer(data= request.data,instance =task)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['GET'])
def detailview(request,pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteview(request,pk):
    tasks = Task.objects.get(pk=pk)
    tasks.delete()
    return Response('Delete Successfully')