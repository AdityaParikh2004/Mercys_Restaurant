from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializers

@api_view(['GET'])
def getById(request, id):
    item = Item.objects.filter(id=id).first()
    item_data = ItemSerializers(item).data
    if item is None:
        response_data = {"response":"Item does not exist"}
        return Response(response_data,status=status.HTTP_404_NOT_FOUND)
    response_data = {"response":item_data}
    return Response(response_data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getbyname(request,waiter_name):
    items = Item.objects.filter(waiter_name=waiter_name).all()
    item_data = ItemSerializers(items, many=True).data
    if items is None:
        response_data = {"response":"Item does not exist"}
        return Response(response_data,status=status.HTTP_404_NOT_FOUND)
    response_data = {"response":item_data}
    return Response(response_data,status=status.HTTP_200_OK)