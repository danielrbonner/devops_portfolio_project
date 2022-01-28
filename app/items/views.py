from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from items.models import Item
from items.serializers import ItemSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "programs/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Item.objects.all()
    return render(request, "items/index.html", {'items': queryset})


""" 
class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'items/index.html'

    def get(self, request):
        queryset = Item.objects.all()
        return Response({'items': queryset})


class list_all_items(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'items/item_list.html'

    def get(self, request):
        queryset = Item.objects.all()
        return Response({'items': queryset}) """


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def item_list(request):
    if request.method == 'GET':
        items = Item.objects.all()

        item_id = request.GET.get('item id', None)
        if item_id is not None:
            items = items.filter(item_id__icontains=item_id)

        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse(item_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(item_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Item.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} programs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return JsonResponse({'message': 'The item does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        item_serializer = ItemSerializer(item)
        return JsonResponse(item_serializer.data)

    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse(item_serializer.data)
        return JsonResponse(item_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return JsonResponse({'message': 'item was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def item_list_open(request):
    items = Item.objects.filter(status="open")

    if request.method == 'GET':
        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)