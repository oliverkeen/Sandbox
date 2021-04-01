from django.urls import path
from . import views

app_name = "polls" # Sets application namespace

# Creates list of URL patterns corresponding to various view functions
urlpatterns = [
    # /polls
    path("", views.IndexView.as_view(), name="index"),

    # /polls/3
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    #/polls/3/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # /polls/3/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]