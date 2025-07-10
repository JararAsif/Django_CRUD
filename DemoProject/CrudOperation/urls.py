from django.urls import path
from .views import Home,Add_Student,Delete_Student,Update_Record,main_page

urlpatterns = [
    path('',main_page.as_view(),name='home'),
    path('add_student/', Add_Student.as_view(), name= 'add_student'),
    path('delete_student/',Delete_Student.as_view(),name='delete_student'),
    path('update_student/<int:id>/',Update_Record.as_view(),name='update_student'),
    path('department_detail/<int:code>',Home.as_view(),name='department_detail'),
]