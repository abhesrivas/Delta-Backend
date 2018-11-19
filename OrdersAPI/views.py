from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from OrdersAPI.models import *
from OrdersAPI.serializers import *
from django.http import Http404
from . import recommendation_history as rec

# Lists all orders or creates a new one
class OrderList(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

    def post(self, request):
        print('Self = ',self)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet)

        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for Quote

class QuoteList(APIView):

    def get(self, request):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)

        return Response(serializer.data)

    def post(self, request):
        print('Self = ',self)
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('----------Quote is saved--------')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuoteDetail(APIView):

    def get_object(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
#        print('Snippet = ', snippet)
        serializer = QuoteSerializer(snippet)

        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = QuoteSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class RecommendedList(APIView):

    def get(self,request):
        return Response(rec.get_recommendations([552,97,1182,211,1010]))
