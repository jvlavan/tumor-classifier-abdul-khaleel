from django.urls import path
from . import views

urlpatterns = [
    path('', views.classify_mri, name='classify_mri'),
    path('result/', views.classify_mri, name='result'),
]
