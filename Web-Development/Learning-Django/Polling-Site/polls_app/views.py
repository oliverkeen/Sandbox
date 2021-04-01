from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from django.http import HttpResponse, Http404

from .models import Question, Choice

# Houses functions and classes that handle what data displays in HTML templates
# Create your views here.

"""
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    ## template = loader.get_template("polls_app/index.html")
    context = {"latest_question_list": latest_question_list}

    ## return HttpResponse(template.render(context, request))
    return render(request, "polls_app/index.html", context)

def detail(request, question_id):

    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist!")
    
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls_app/detail.html", {"question": question})

def results(request, question_id): # Redundant to above detail view
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls_app/results.html", {"question": question})
"""

class IndexView(generic.ListView):
    template_name = "polls_app/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls_app/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls_app/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        # Redisplays question voting form
        return render(request, "polls_app/detail.html", {
            "question": question,
            "error_message": "Please select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    
        # Always returns HttpResponseRedirect after successfully dealing
        # with POST data, preventing data from being posted twice if user
        # hits Back button
        no = HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
        return no