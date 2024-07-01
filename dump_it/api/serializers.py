from rest_framework import serializers
from .models import Item

class ItemSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['id','order','waiter_name','meal_cost','tip_cost']
    