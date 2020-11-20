from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import *
from api.serializers import DepremSerializer
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django.core.cache import cache

class DepremView(APIView,LimitOffsetPagination):
    def get(self,request,format=None):
        if cache.get("deprem"):
            veriler = cache.get("deprem")
        else:
            veriler = get_veriler()
            cache.set("deprem",veriler,60*2)
            
        results = self.paginate_queryset(veriler,request,self)
        s = DepremSerializer(results,many=True)
        return self.get_paginated_response(s.data)

