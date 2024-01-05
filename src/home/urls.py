from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('add-task/', views.addTask, name='addTask'),
    path('edit-task/<int:task_id>/', views.editTask, name='editTask'),
    path('delete-task/<int:task_id>/', views.deleteTask, name='deleteTask'),
    path('update-task-status/', views.updateTaskStatus, name='update_task_status'),

]