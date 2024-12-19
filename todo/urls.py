from django.urls import path
from todo import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create-task/', views.create_task, name='create-task'),
    path('apend-task/<int:pk>/', views.append_task, name='append-task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),
    path('update-task-status/<int:pk>/', views.change_status, name='update-task-status'),

    
]
