from django.urls import path 

from home import views

urlpatterns = [
    path('', views.index),
    path('api/submit', views.ImageGeneratorAPI.as_view())
]