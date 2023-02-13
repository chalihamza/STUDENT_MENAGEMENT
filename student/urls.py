from django.urls import path, include
from . import views

urlpatterns = [
    path('add_student', views.add_student, name='add_student'),
    path('view_student', views.view_student, name='view_student'),
    path('edit_student/<str:id>', views.edit_student, name='edit_student'),
    path('update_student', views.update_student, name='update_student'),
    path('delete_student/<str:admin>', views.delete_student, name='delete_student'),
]