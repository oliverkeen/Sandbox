from django.urls import path
from . import views

# Creates list of URL patterns corresponding to various view functions
urlpatterns = [
    path("", views.index, name="index")
]