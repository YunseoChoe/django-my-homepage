from django.urls import path
from .views import BoardCreateAPIView
from .views import BoardUpdateAPIView


urlpatterns = [
    path('boardcreate/', BoardCreateAPIView.as_view()),
    path('boardupdate/<int:pk>/', BoardUpdateAPIView.as_view()),
]