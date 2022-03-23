from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def stu_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parse_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=parse_data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Data Inserted'}
            j_data=JSONRenderer().render(msg)
            return HttpResponse(j_data,content_type='application/json')
        else:
            errors=JSONRenderer().render(serializer.errors)
            return HttpResponse(errors,content_type='application/json')