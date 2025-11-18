from django.urls import path
from . import views

urlpatterns = [
    path('', views.logedin_home, name='Homepage'),  
    path('/create_todo', views.create_todo, name='create_todo'),
    path('details/<int:todo_id>', views.details, name='details'),
    path('delete/int:<todo_id>',views.delete,name='delete'),
    path('update/int: <todo_id>',views.update,name='update'),
]
