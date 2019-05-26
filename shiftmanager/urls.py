from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/employee/', views.EmployeeListCreate.as_view()),
    path('api/shift/', views.ShiftListCreate.as_view()),
    path('api/roster/', views.RosterListCreate.as_view()),
    path('upload/', views.upload_csv, name='upload_csv'),
]
