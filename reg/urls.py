from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('register/' ,views.register ,name='register'),
    path('login/' ,views.login, name='login'),
    path('logout/' ,views.logout, name='logout'),
    path('home/' ,views.home, name='home'),
    path('profile',views.profile, name='profile'),
    path('department/' ,views.department_view , name='department'),
    path('teacher/',views.teacher_view,name='teacher'),
    path('student/',views.student_view,name='student'),
    path('ddetails',views.ddetails,name='ddetails'),
    path('delete/<int:did>/',views.delete,name='Delete'),
    path('update/<int:did>/',views.update,name='update')
  ]