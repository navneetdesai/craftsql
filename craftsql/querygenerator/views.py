from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

from . import cohere_helper
from .models import UserActivity, Functionality

# Display last 50% records from Employee table
from . import analysis




def index(request):
    return render(request, 'index.html')


def querypage(request):
    f = Functionality.objects.filter(name='generate')[0]
    update_user_activity(request, f)
    return render(request, 'querypage.html')



def update_user_activity(request, func):
    # print(f'\n{func}\n')
    user_activity = UserActivity(functionality=func, timestamp=datetime.now())
    user_activity.save()


def explain_page(request):
    f = Functionality.objects.filter(name='explain_sql')[0]
    update_user_activity(request, f)
    return render(request, 'explainpage.html')


def fixpage(request):
    f = Functionality.objects.filter(name='fix_query')[0]
    update_user_activity(request, f)
    return render(request, 'fixpage.html')


def suggest(request):
    f = Functionality.objects.filter(name='suggest_optimization')[0]
    update_user_activity(request, f)
    return render(request, 'suggest.html')

@cache_page(60 * 15)
def generate(request):
    if request.method == 'POST':
        query_input = request.POST.get('query-input')
        if not query_input:
            return render(request, 'querypage.html')
        response = cohere_helper.generate_query(query_input)
        return render(request, 'querypage.html', {'results': response.generations[0].text})
    return render(request, 'querypage.html', {'results': 'No query generated yet.'})

@cache_page(60 * 15)
def explain_sql(request):
    if request.method != 'POST':
        return render(request, 'explain.html')
    query = request.POST.get('query', '')
    if not query:
        return render(request, 'explain.html')
    response = cohere_helper.explain_query(query)
    return render(request, 'explainpage.html', {'explanation': response[0].text})

@cache_page(60 * 15)
def fix_query(request):
    if request.method != 'POST':
        return render(request, 'fixpage.html')
    query = request.POST.get('query', '')
    if not query:
        return render(request, 'fixpage.html')
    response = cohere_helper.fix_query(query)
    return render(request, 'fixpage.html', {'results': response[0].text})

@cache_page(60 * 15)
def suggest_optimization(request):
    if request.method != 'POST':
        return render(request, 'suggest.html')
    query = request.POST.get('query-input', '')
    if not query:
        return render(request, 'suggest.html')
    response = cohere_helper.suggest_optimizations(query)
    suggestions = response[0].text.split('\n')
    suggestions = list(set(suggestions))

    return render(request, 'suggest.html', {'results': '\n'.join(suggestions)})

