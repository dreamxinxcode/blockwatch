from . import views
from django.urls import path, include
from django.views.generic import TemplateView

app_name = "main"

urlpatterns = [
    path('', views.homepage_view, name='homepage_view'),
]
