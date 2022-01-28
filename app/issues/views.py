from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from issues.models import Issue
from issues.serializers import IssueSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "programs/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Issue.objects.all()
    return render(request, "issues/index.html", {'issues': queryset})


""" 
class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'issues/index.html'

    def get(self, request):
        queryset = Issue.objects.all()
        return Response({'issues': queryset})


class list_all_issues(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'issues/issue_list.html'

    def get(self, request):
        queryset = Issue.objects.all()
        return Response({'issues': queryset}) """


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def issue_list(request):
    if request.method == 'GET':
        issues = Issue.objects.all()

        issue_id = request.GET.get('issue id', None)
        if issue_id is not None:
            issues = issues.filter(issue_id__icontains=issue_id)

        issues_serializer = IssueSerializer(issues, many=True)
        return JsonResponse(issues_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        issue_data = JSONParser().parse(request)
        issue_serializer = IssueSerializer(data=issue_data)
        if issue_serializer.is_valid():
            issue_serializer.save()
            return JsonResponse(issue_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(issue_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Issue.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} programs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def issue_detail(request, pk):
    try:
        issue = Issue.objects.get(pk=pk)
    except Issue.DoesNotExist:
        return JsonResponse({'message': 'The issue does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        issue_serializer = IssueSerializer(issue)
        return JsonResponse(issue_serializer.data)

    elif request.method == 'PUT':
        issue_data = JSONParser().parse(request)
        issue_serializer = IssueSerializer(issue, data=issue_data)
        if issue_serializer.is_valid():
            issue_serializer.save()
            return JsonResponse(issue_serializer.data)
        return JsonResponse(issue_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        issue.delete()
        return JsonResponse({'message': 'issue was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def issue_list_open(request):
    issues = Issue.objects.filter(status="open")

    if request.method == 'GET':
        issues_serializer = IssueSerializer(issues, many=True)
        return JsonResponse(issues_serializer.data, safe=False)