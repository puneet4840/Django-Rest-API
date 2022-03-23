from django.shortcuts import render
from django.http import HttpResponse
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

## Single object data
def student_details(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


## Query Set - All Student Data
def student_detail(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/data')