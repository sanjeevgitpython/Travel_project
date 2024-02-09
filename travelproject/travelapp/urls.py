from . import views
from django.urls import path

urlpatterns = [

    path('',views.fun,name='demo'),
    # path('add/',views.addition,name='add')
]