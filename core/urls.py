from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('register/', views.register_volunteer, name='register_volunteer'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/export/', views.export_volunteer_report, name='export_volunteer_report'), 
    path('events/', views.event_list, name='event_list'),
]