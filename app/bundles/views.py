from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from bundles.models import Bundle
from bundles.serializers import BundleSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "programs/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Bundle.objects.all()
    return render(request, "bundles/index.html", {'bundles': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bundles/index.html'

    def get(self, request):
        queryset = Bundle.objects.all()
        return Response({'bundles': queryset})


class list_all_bundles(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bundles/bundle_list.html'

    def get(self, request):
        queryset = Bundle.objects.all()
        return Response({'bundles': queryset})


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def bundle_list(request):
    if request.method == 'GET':
        bundles = Bundle.objects.all()

        bundle_id = request.GET.get('bundle id', None)
        if bundle_id is not None:
            bundles = bundles.filter(bundle_id__icontains=bundle_id)

        bundles_serializer = BundleSerializer(bundles, many=True)
        return JsonResponse(bundles_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        bundle_data = JSONParser().parse(request)
        bundle_serializer = BundleSerializer(data=bundle_data)
        if bundle_serializer.is_valid():
            bundle_serializer.save()
            return JsonResponse(bundle_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(bundle_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Bundle.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} programs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def bundle_detail(request, pk):
    try:
        bundle = Bundle.objects.get(pk=pk)
    except Bundle.DoesNotExist:
        return JsonResponse({'message': 'The bundle does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        bundle_serializer = BundleSerializer(bundle)
        return JsonResponse(bundle_serializer.data)

    elif request.method == 'PUT':
        bundle_data = JSONParser().parse(request)
        bundle_serializer = BundleSerializer(bundle, data=bundle_data)
        if bundle_serializer.is_valid():
            bundle_serializer.save()
            return JsonResponse(bundle_serializer.data)
        return JsonResponse(bundle_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bundle.delete()
        return JsonResponse({'message': 'bundle was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def bundle_list_open(request):
    bundles = Bundle.objects.filter(status="open")

    if request.method == 'GET':
        bundles_serializer = BundleSerializer(bundles, many=True)
        return JsonResponse(bundles_serializer.data, safe=False)
