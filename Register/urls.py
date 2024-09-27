
from django.urls import path , include
from . import views 

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'register', EmployeeViewSet)  # Register the viewset with a router

urlpatterns = [

# Fuction based View
    path('EmployeeView/',views.EmployeeView),

#class based view

    path('EmployeeViewClass/',views.EmployeeViewClass.as_view())




]+router.urls # View Set Router
