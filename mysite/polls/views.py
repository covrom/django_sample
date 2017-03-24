from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question,Choice

def index(request):
    #pylint: disable=no-member
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context, request))
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question': question})


def results(request, question_id):
    response = 'Вы смотрите результаты вопроса %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #снова покажем форму голосования
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"Вы не отметили пункт",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #всегда возвращаем HttpResponseRedirect после корректной обработки POST запроса
        #это защитит от двойной записи данных, если пользователь вернулся назад
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
