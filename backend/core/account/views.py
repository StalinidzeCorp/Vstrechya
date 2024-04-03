from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class testingAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'key': "Hello World"})


def test(request):
    return HttpResponse('test page')
