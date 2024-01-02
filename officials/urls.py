from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="officials_home"),

    # Assignors
    path('assignor/', views.assignor_home, name="assignor_home"),
]
