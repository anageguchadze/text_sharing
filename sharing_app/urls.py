from django.urls import path
from .views import index, edit

urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>/', edit, name='edit'),
]