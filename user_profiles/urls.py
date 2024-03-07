from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('<int:pk>/', ProductDetailsView.as_view()),
    path('<int:pk>/delete/', ProductDeleteView.as_view()),
]