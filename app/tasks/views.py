from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "programs/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Task.objects.all()
    return render(request, "tasks/index.html", {'tasks': queryset})


""" 
class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tasks/index.html'

    def get(self, request):
        queryset = Task.objects.all()
        return Response({'tasks': queryset})


class list_all_tasks(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tasks/task_list.html'

    def get(self, request):
        queryset = Task.objects.all()
        return Response({'tasks': queryset}) """


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()

        task_id = request.GET.get('task id', None)
        if task_id is not None:
            tasks = tasks.filter(task_id__icontains=task_id)

        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(task_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Task.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} programs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'message': 'The task does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        task_serializer = TaskSerializer(task)
        return JsonResponse(task_serializer.data)

    elif request.method == 'PUT':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(task, data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data)
        return JsonResponse(task_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'task was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def task_list_open(request):
    tasks = Task.objects.filter(status="open")

    if request.method == 'GET':
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)