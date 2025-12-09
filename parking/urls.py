from django.urls import path
from . import views

app_name = 'parking'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('andar/<str:name>/', views.floor_detail, name='floor_detail'),
]
