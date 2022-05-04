from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request): 
        return Response(data="Hello, World !", status=200)
    def patch(self, request):
        return Response(data="Hola, estoy en el patch", status=200)

    def delete(self, request):
        return Response(data="Hola, estoy en el delete", status=200)

    def post(self, request):
        return Response(data="Hola, estoy en el post", status=200)

class PetListAPIView(ListAPIView):
    def get(self, request):
        return Response(data="Hola a todos estas son mis mascotas", status=200)

class PetAPIView(RetrieveAPIView):
    def get(self,request):
        return Response(data="Hola, estoy en el get del petview", status=200)


