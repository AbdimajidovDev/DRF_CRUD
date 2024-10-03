from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializers import *


class HotelView(APIView):
    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        serializers = HotelSerializer(hotels, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = HotelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelDetailView(APIView):
    def get_object(self, pk):
        try:
            return Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hotel = self.get_object(pk=pk)
        serializers = HotelSerializer(hotel, many=False)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        hotel = self.get_object(pk=pk)
        serializers = HotelSerializer(hotel, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hotel = self.get_object(pk=pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
