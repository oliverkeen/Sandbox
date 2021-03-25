from django.urls import path
from hello_world_app import views

# Creates list of URL patterns corresponding to various view functions
urlpatterns = [
    path("", views.hello_world, name="hello_world"),
]
