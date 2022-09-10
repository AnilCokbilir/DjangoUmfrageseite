from http.client import HTTPS_PORT
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Poll
from django.urls import reverse
def index(request):
    context = {'umfragen': Poll.objects.all(), 'title': 'Umfragenseite'}
    return render(request=request, template_name='polls/index.html', context=context)

def umfrage_detail(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage}
    return render(request=request, template_name='polls/umfrage.html', context=context)

def vote(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    try:
        ausgewaehlte_antwort = umfrage.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("Fehler: keine bzw. eine ungültige Antwort ausgewählt!")
    else:
        ausgewaehlte_antwort.votes += 1
        ausgewaehlte_antwort.save()
        return HttpResponseRedirect(reverse('results', args=(umfrage.slug,)))

def results(request,slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage}
    return render(request=request, template_name='polls/results.html', context=context)