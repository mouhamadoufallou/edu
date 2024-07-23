from django.contrib import admin
from django.urls import path
from employe import views  

urlpatterns = [
    path('show_employes', views.show_employes, name='show_employes'),  
    path('add_employe',views.add_employe, name='add_employe'),  
    path('edit_employe/<int:id>', views.edit_employe, name='edit_employe'),  
    path('update_employe/<int:id>', views.update_employe, name='update_employe'),  
    path('delete_employe/<int:id>', views.destroy_employe, name='destroy_employe'),  
]