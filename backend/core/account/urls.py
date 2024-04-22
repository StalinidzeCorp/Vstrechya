from django.urls import path
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
# from .views import testingAPI

urlpatterns = [
    # path('test/', views.test),
    # path('apitest/', testingAPI.as_view()),

    path('auth/signup/', UserViewSet.as_view({'post': 'create'}), name="register"),
    path('auth/signin/', TokenObtainPairView.as_view(), name="create-token"),
    path('auth/api/token/refresh/', TokenRefreshView.as_view(), name="refresh-token"),
]