from django.urls import path
from . import views
urlpatterns = [
    path('helloword', views.helloword),
    path('', views.taskList, name='task-List'),
    path('task/<int:id>', views.taskview, name="task-view"),
    path('newtask/', views.newtask, name='new-task'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]
