from django.urls import path
from api import views

urlpatterns=[
    path('stu_create/',views.stu_create),
]