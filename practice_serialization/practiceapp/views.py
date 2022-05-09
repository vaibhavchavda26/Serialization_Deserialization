from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    #print(stu)
    serializer = StudentSerializer(stu)
    #print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type = 'application/json')

    #return JsonResponse(serializer.data)

def student_list(request):
    stu = Student.objects.all()
    #print(stu)
    serializer = StudentSerializer(stu, many = True)
    #print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type = 'application/json')
    
    #return JsonResponse(serializer.data, safe=False)