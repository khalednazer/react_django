from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import BasicAuthentication
from django.views.generic import TemplateView

from .models import Task
# Create your views here.

@api_view(['GET'])
@authentication_classes([AllowAny])
@permission_classes([AllowAny])
def apiOverview(request):
	
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)
	

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST', 'GET'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return render(request, 'create.html', {})
	# return render(request, 'هل استطيع ان اضع هنا صفحه رياكت و كي', {})
	
class ReactAppView(TemplateView):
    template_name = "create.html"

class Khaled(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer


@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')