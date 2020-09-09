from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import *
from api.serializers import DepremSerializer
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

class DepremView(APIView,LimitOffsetPagination):
    def get(self,request,format=None):
        veriler = get_veriler()
        results = self.paginate_queryset(veriler,request,self)
        s = DepremSerializer(results,many=True)
        return self.get_paginated_response(s.data)

