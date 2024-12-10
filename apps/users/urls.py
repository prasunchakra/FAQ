from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("", view=views.ListView.as_view(), name="list"),
]