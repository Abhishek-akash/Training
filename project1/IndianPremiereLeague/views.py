from django.shortcuts import render
from IndianPremiereLeague.models import Team
from rest_framework.response import Response
from rest_framework.views import APIView

class IPL(APIView):
    def get(self, request):
        x = int(request.GET.get('x'))
        y = int(request.GET.get('y'))

        queryset = Team.objects.all().values()
        return Response({"success":True,"data":x + y})

    def post(self,request):
        # import pdb;pdb.set_trace()

        name = request.data.get('name', None)
        size = request.data.get('size', None)
        captain = request.data.get('captain', None)
        # password = request.data.get('password', None)
        # res =True if username in Team.objects.all().values_list('name',flat=True) else False

        t = Team.objects.create(name=name,size=size,captain=captain)
        
        res =  {
            'name':t.name,
            'size':t.size,
            'captain':t.captain
        }
        return Response({"success":True,'data':res})
        