from django.shortcuts import render
from User.models import *
from rest_framework.views import APIView 
from rest_framework import viewsets
from rest_framework.response import Response
from User.serializers import StudentSerializer

# Create your views here.
class StudentView(viewsets.ViewSet):
    
    queryset = Student.objects.all()
    serializer = StudentSerializer

    def list(self, request):
        try: 
            serializer = self.serializer(self.queryset, many = True)
            return Response(serializer.data)

        except Exception as e:
            return Response({'error':str(e)})

    def retrieve(self, request, pk):
        try:
            qs2 = self.queryset.get(pk = int(pk))
            serializer = self.serializer(qs2)
            return Response(serializer.data)

        except Exception as e:
            return Response({'error':str(e)})
    
    def create(self, request):
        try:
            data = dict()
            data['name'] = request.data['name']
            data['teacher'] = int(request.data['teacher_id'])
            data['sub'] = int(request.data['subject_id'])
            
            serializer = self.serializer(data = data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response({"error":serializer.errors})

        except Exception as e:
            return Response({'error':str(e)})

    def partial_update(self, request, pk = None):

        try:
            student_object = self.queryset.get(pk = pk)
            data = request.data.dict()
             
        except Exception as e:
            return Response({'error':str(e)})

class TeachersView(APIView):
    def get(self,request):
        try:
            query= Teacher.objects.all().values()
            return Response(query)
        except Exception as e:
            return Response({'error':str(e)})

    def put(self,request):
        try:
            query= Teacher.objects.filter().update(name='Gannu')
            return Response(query)
        except Exception as e:
            return Response({'error':str(e)})
