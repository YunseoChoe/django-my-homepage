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
    # <POST 요청을 처리하는 역할>
    def post(self, request): # post 이름 바꾸려면 어떻게 해야 돼
        # (클라이언트로부터 전달된) 데이터 추출
        title = request.data.get('title')
        content = request.data.get('content')
        writer = request.data.get('writer')

        # Board 모델 인스턴스 생성
        board_instance = Board(title=title, content=content, writer=writer)

        # 모델 인스턴스를 데이터베이스에 저장
        board_instance.save() # save()는 django에서 제공해주는 메서드

        # (저장된 데이터를 시리얼라이저를 통해 응답)
        # 생성된 Board 객체를 시리얼라이저의 인스턴스로 전달하고,
        # serializer.data를 통해 시리얼라이저화된 데이터를 가져온 후 응답
        serializer = BoardSerializers(board_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# update

# update
class BoardUpdateAPIView(APIView):
    # <PATCH 요청을 처리하는 역할>
    def patch(self, request, pk): # 함수 이름이 중요해..?
        try:
            # 게시판을 찾음
            board_instance = Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            return Response({"message": "게시판이 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        # (클라이언트로부터 전달된) 데이터 추출
        title = request.data.get('title')
        content = request.data.get('content')
        writer = request.data.get('writer')

        # 데이터를 부분적으로 업데이트
        if title:
            board_instance.title = title
        if content:
            board_instance.content = content
        if writer:
            board_instance.writer = writer
        # 모델 인스턴스를 데이터베이스에 저장
        board_instance.save() # save()는 django에서 제공해주는 메서드

        # 시리얼라이저를 통해 응답
        serializer = BoardSerializers(board_instance)
        return Response(serializer.data)

# delete
class BoardDeleteAPIView(APIView):
    # <DELETE 요청을 처리하는 역할>
    def delete(elf, request, pk):
        try:
            # 게시판을 찾음
            board_instance = Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            return Response({"message": "게시판이 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        # 게시판 삭제
        board_instance.delete() # delete()는 django에서 제공해주는 메서드

        response = HttpResponse("게시판이 삭제되었습니다.")
        # return Response({"message": "게시판이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        return response

# read 



'''
Django REST Framework에서는 HTTP 요청 방식에 따라 메서드 이름을 지정해야 합니다.

일반적으로 RESTful API에서는 다음과 같은 HTTP 요청 방식과 메서드의 관계가 있습니다:

GET: 리소스의 조회. 일반적으로 get 메서드로 처리합니다.
POST: 새로운 리소스의 생성. 일반적으로 create 메서드로 처리합니다.
PUT: 리소스의 전체적인 수정. 일반적으로 update 메서드로 처리합니다.
PATCH: 리소스의 일부 수정. 일반적으로 partial_update 메서드로 처리합니다.
DELETE: 리소스의 삭제. 일반적으로 destroy 메서드로 처리합니다.
'''
