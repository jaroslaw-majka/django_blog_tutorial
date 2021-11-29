from django.http import HttpResponse

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-publication_date')[:5]
    output = '<p> '.join([question.question for question in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
