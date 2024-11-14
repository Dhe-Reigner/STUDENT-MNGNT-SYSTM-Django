from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
]