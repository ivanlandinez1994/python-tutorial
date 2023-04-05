from django.urls import path, include
from .views import CommentsAPIView, GetCommentsAPIView

urlpatterns = [
    path('posts/<str:pk>/comments', GetCommentsAPIView.as_view()),
    path('comments', CommentsAPIView.as_view())
]
