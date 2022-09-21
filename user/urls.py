from django.urls import path
from user import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
