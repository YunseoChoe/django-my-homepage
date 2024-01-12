from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView        
from rest_framework import status
from django.http import HttpResponse
from .models import Board
from rest_framework import generics
from .serializers import BoardSerializers

# create
class BoardCreateAPIView(APIView):
    def post(self, request):
        # 데이터 추출
        title = request.data.get('title')
        content = request.data.get('content')
        writer = request.data.get('writer')

        # Board 모델 인스턴스 생성
        board_instance = Board(title=title, content=content, writer=writer)

        # 모델 인스턴스를 데이터베이스에 저장
        board_instance.save()

        # 저장된 데이터를 시리얼라이저를 통해 응답
        serializer = BoardSerializers(board_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# read 

# update

# delete