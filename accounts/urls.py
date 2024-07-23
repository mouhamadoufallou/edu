from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.user_logout, name='user_logout'),
    path('add_user/', views.add_user, name='add_user'),
    path('adminpage/', views.admin, name='adminpage'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
]