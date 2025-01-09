from django.urls import path
from . import views

urlpatterns = [
    path('', views.getdata, name='getdata'),
    path('add/', views.addPerson, name='addPerson'),
    path('student/', views.getstudentdata, name='getstudentdata'),
    path('addstudent/', views.addStudent, name='addStudent'),
    path('students/update/<int:pk>/', views.updateStudent, name='updateStudent'),

]
