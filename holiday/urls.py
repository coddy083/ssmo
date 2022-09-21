from django.urls import path
from holiday import views

urlpatterns = [
    path('working/', views.HolidayView.as_view()),
]
