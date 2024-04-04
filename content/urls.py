from django.urls import path
from .views import index , add_task, delete_task ,mark
urlpatterns = [
    path('', index, name="index"),
    path('add_task/', add_task, name="add_task"),
    path('delete_task/<int:task_id>/', delete_task, name="delete_task"),
    path('mark/<int:id>',  mark, name="mark"),
]