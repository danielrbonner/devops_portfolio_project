from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from programs.models import Program
from programs.serializers import ProgramSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "programs/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Program.objects.all()
    return render(request, "programs/index.html", {'programs': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'programs/index.html'

    def get(self, request):
        queryset = Program.objects.all()
        return Response({'programs': queryset})


class list_all_programs(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'programs/program_list.html'

    def get(self, request):
        queryset = Program.objects.all()
        return Response({'programs': queryset})


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def program_list(request):
    if request.method == 'GET':
        programs = Program.objects.all()

        program_id = request.GET.get('program_id', None)
        if program_id is not None:
            programs = programs.filter(program_id__icontains=program_id)

        programs_serializer = ProgramSerializer(programs, many=True)
        return JsonResponse(programs_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        program_data = JSONParser().parse(request)
        program_serializer = ProgramSerializer(data=program_data)
        if program_serializer.is_valid():
            program_serializer.save()
            return JsonResponse(program_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(program_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Program.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} programs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def program_detail(request, pk):
    try:
        program = Program.objects.get(pk=pk)
    except Program.DoesNotExist:
        return JsonResponse({'message': 'The program does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        program_serializer = ProgramSerializer(program)
        return JsonResponse(program_serializer.data)

    elif request.method == 'PUT':
        program_data = JSONParser().parse(request)
        program_serializer = ProgramSerializer(program, data=program_data)
        if program_serializer.is_valid():
            program_serializer.save()
            return JsonResponse(program_serializer.data)
        return JsonResponse(program_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        program.delete()
        return JsonResponse({'message': 'program was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def program_list_open(request):
    programs = Program.objects.filter(status="open")

    if request.method == 'GET':
        programs_serializer = ProgramSerializer(programs, many=True)
        return JsonResponse(programs_serializer.data, safe=False)
