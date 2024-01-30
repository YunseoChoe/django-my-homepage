from rest_framework import serializers
from .models import Board

# create
# 클라이언트로부터 전달받은 데이터를 Board 모델의 인스턴스로 변환하여 데이터를 저장
class BoardSerializers(serializers.ModelSerializer): 
    class Meta:
        model = Board
        fields = ['title', 'content', 'writer']
    
    # 시리얼라이저가 POST 요청 등으로부터 전달받은 데이터를 기반으로 새로운 Board 객체를 생성하는 역할
    def create(self, validated_data):
        board = Board(**validated_data)
        board.save()
        return board