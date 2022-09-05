from django.urls import include, path
from Employee import views

urlpatterns = [
    path('', views.EmployeeView.as_view()),
]