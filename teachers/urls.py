from django.contrib import admin
from django.urls import path
from teachers import views  
 
urlpatterns = [
    path('show_teacher', views.show_teacher, name='show_teacher'),  
    path('add_teacher',views.add_teacher, name='add_teacher'),  
    path('edit_teacher/<int:id>', views.edit_teacher, name='edit_teacher'),  
    path('update_teacher/<int:id>', views.update_teacher, name='update_teacher'),  
    path('destroy_teacher/<int:id>', views.destroy_teacher, name='destroy_teacher'), 
    path('detail_teacher/<int:id>/', views.detail_teacher, name='detail_teacher'), 
]