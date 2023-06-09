from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse


# Create your views here.
def index(request):
    latest_question_list=Question.objects.all()
    return render(request,"polls/index.html",{
        "latest_question_list":latest_question_list
    })



def detail(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{
        "question":question
    })

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html",{
            "questio":question,
            "error_message":"No hay voto"
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:index",args=()))

