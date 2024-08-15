from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    

    # URLs pour la réinitialisation du mot de passe
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('', views.index, name='index'),
    path('signup/', views.add_user, name='add_user'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.user_logout, name='user_logout'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
]
