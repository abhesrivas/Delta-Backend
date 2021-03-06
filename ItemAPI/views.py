from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ItemAPI.models import *
from ItemAPI.serializers import *
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from . import LocationRecommendation as recommendation
from . import recommendation_history as rec

# Lists all laptops
class LaptopList(APIView):
    def get(self, request):
        laptops = Laptop.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(laptops, request)
        serializer = LaptopSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

# Get individual laptop details
class LaptopDetail(APIView):

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = LaptopSerializer(snippet)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Laptop.objects.get(pk=pk)
        except Laptop.DoesNotExist:
            raise Http404


# Get Recommended List Based On Location, Sector Type
class LocationRecommendation(APIView):
    def get(self,request):
        return Response(recommendation.location_similarity(self.location, self.company_type))

# Get Recommended List Based on History
class RecommendedList(APIView):
    def get(self,request):
        return Response(rec.get_recommendations([552,97,1182,211,1010]))


