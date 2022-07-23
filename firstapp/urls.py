
from django.urls import path
from . import views

urlpatterns=[
    path('khafan' , views.index),
    path('<day>', views.dynamic_day),

]