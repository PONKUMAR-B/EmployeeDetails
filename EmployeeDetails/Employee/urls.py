from django.urls import include, path
from Employee import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('edetails', views.EmployeeView)


urlpatterns = [
    path('crud', views.EmployeeView.as_view()),
]