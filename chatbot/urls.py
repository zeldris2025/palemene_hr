from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_home, name='chatbot_home'),
    path('get_employee/', views.get_employee, name='get_employee'),
    path('leave_balance/<str:employee_id>/', views.leave_balance, name='leave_balance'),
    path('download_leave_form/', views.download_leave_form, name='download_leave_form'),
    path('download_leave_form/file', views.serve_leave_form_file, name='serve_leave_form_file'),
]
