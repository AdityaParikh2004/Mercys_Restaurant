from rest_framework import status
from rest_framework.views import APIView,Response
from .models import Item
from .serializers import ItemSerializers

class DumpItAPI(APIView):
    
    def get(self,request):
        items = Item.objects.all()
        items_data = ItemSerializers(items,many=True).data
        response_data = {"datas":items_data}
        return Response(response_data,status=status.HTTP_200_OK)
    
    def post(self,request):
        order = request.data.get('order')
        meal_cost = request.data.get('meal_cost')
        waiter_name = request.data.get('waiter_name')
        tip_cost = request.data.get('tip_cost')
        tip_percentage = ((tip_cost/meal_cost)*100)
        Item.objects.create(order = order, meal_cost = meal_cost, waiter_name = waiter_name, tip_cost = tip_cost, tip_percentage = tip_percentage)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        order = request.data.get('order')
        tip_cost = request.data.get('tip_cost')
        meal_cost = request.data.get('meal_cost')
        tip_percentage = ((tip_cost/meal_cost)*100)
        item = Item.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exist"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.order = order
        item.tip_cost = tip_cost
        item.tip_percentage = tip_percentage
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        item = Item.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exist"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
    
        item.delete()
        response_data = {"response":"item Deleted"}
        return Response(response_data,status=status.HTTP_200_OK)
    
    def retrieve(self,request,id):
        item = Item.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exist"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        response_data = {"response":item}
        return Response(response_data,status=status.HTTP_200_OK)
        