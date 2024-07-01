from django.db import models

class Item(models.Model):
    order=models.TextField()
    meal_cost=models.FloatField()
    waiter_name=models.TextField()
    tip_cost=models.FloatField()
    tip_percentage=models.FloatField()