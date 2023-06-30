from dj_rest_auth.views import LoginView
from django.urls import path, include
# from dj_rest_auth import LoginView
from account import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('register/',  views.UserRegiseterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', views.CustomLogout.as_view()),
    path('', include(router.urls))
    # path('', views.UserListView.as_view()),
    # path('<int:pk>/', views.UserListViewDetailView.as_view()),
]