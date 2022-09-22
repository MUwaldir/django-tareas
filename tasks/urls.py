
from django.urls import path,include
from tasks import views
app_name = 'djangocrud'

urlpatterns = [
    path('', views.home , name='home'),
    path('home/', views.home, name='home'),
    path('signup/' , views.signup, name='signup'),
    path('tasks/', views.tasks , name='tasks'),
    path('logout/', views.signout , name='logout'),
    path('signin/', views.signin , name='signin'),
    path('create_task/', views.create_task , name='create_task'),
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task_detail/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('task_detail/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('tasks_completed/', views.tasks_completed , name='tasks_completed'),
]
