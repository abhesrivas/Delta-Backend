from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UserAPI.models import *
from UserAPI.serializers import *
from django.http import Http404
from . import dominant

# Lists all users or creates a new one
# users/
class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):
        print('Self = ',self)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            company_name = serializer.data.get('company_name')
#            print(company_name)
            print('----------User is saved--------')
            return Response(dominant.get_dominant_colors(company_name), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet)

        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for Profile

class ProfileList(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)

        return Response(serializer.data)

    def post(self, request):
        print('Self = ',self)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('----------Profile is saved--------')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
#        print('Snippet = ', snippet)
        serializer = ProfileSerializer(snippet)

        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProfileSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

