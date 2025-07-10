from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('celulares/', views.celulares, name='celulares'),
    path('soporte/', views.soporte, name='soporte'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contactanos/', views.contactanos, name='contactanos'),
]