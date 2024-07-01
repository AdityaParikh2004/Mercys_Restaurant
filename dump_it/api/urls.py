from django.urls import path
from .views import DumpItAPI
from .api import getById
from .api import getbyname

urlpatterns = [
    path('',DumpItAPI.as_view()),
    path('create/',DumpItAPI.as_view()),
    path('update/<int:id>/',DumpItAPI.as_view()),
    path('delete/<int:id>/',DumpItAPI.as_view()),
    path('retrieve/<int:id>/',getById),
    path('retrieve2/<str:waiter_name>/',getbyname)
]
