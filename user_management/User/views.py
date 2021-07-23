from django.shortcuts import render
from User.models import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class StudentView(APIView):
    def get(self, request):
        try:
            qs = Student.objects.all().values('id','name','sub__name','teacher__name')
            return Response(qs)
        except Exception as e:
            return Response({'error':str(e)})
