from django.urls import path
from .views import *

urlpatterns = [
  path('dsbaiviet/', dsbaiviet, name='dsbaiviet'),
  path('<int:idbaiviet>/', baiviet, name='suabaiviet'),
  path('', baiviet, name='thembaiviet')
]