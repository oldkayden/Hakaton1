from django.urls import path

from .views import LikeDeleteView, LikeCreateView

urlpatterns = [
    path('', LikeCreateView.as_view()),
    path('<int:pk>/', LikeDeleteView.as_view()),
]