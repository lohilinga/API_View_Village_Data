from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from app.models import *
from app.serializers import *
from rest_framework.response import Response


@api_view(['GET','POST'])
def Vdetails(request):
    VD=VillageData.objects.all()
    VDJSONDATA=VillagemodelSerializers(VD,many=True)
    return Response(VDJSONDATA.data)



