from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_punicao, name='criar_punicao'),
    path('creat/', views.criar_var, name='var'),
]