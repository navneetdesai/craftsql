from django.shortcuts import render
from django.http import HttpResponse
from . import cohere_helper


# Display last 50% records from Employee table

def index(request):
    return render(request, 'index.html')


def querypage(request):
    return render(request, 'querypage.html')


def explain_page(request):
    return render(request, 'explainpage.html')


def fixpage(request):
    return render(request, 'fixpage.html')


def suggest(request):
    return render(request, 'suggest.html')


def generate(request):
    if request.method == 'POST':
        query_input = request.POST.get('query-input')
        if not query_input:
            return render(request, 'querypage.html')
        response = cohere_helper.generate_query(query_input)
        return render(request, 'querypage.html', {'results': response.generations[0].text})
    return render(request, 'querypage.html', {'results': 'No query generated yet.'})


def explain_sql(request):
    if request.method != 'POST':
        return render(request, 'explain.html')
    query = request.POST.get('query', '')
    if not query:
        return render(request, 'explain.html')
    response = cohere_helper.explain_query(query)
    return render(request, 'explainpage.html', {'explanation': response[0].text})


def fix_query(request):
    if request.method != 'POST':
        return render(request, 'fixpage.html')
    query = request.POST.get('query', '')
    if not query:
        return render(request, 'fixpage.html')
    response = cohere_helper.fix_query(query)
    return render(request, 'fixpage.html', {'results': response[0].text})


def suggest_optimization(request):
    if request.method != 'POST':
        return render(request, 'suggest.html')
    query = request.POST.get('query-input', '')
    if not query:
        return render(request, 'suggest.html')
    response = cohere_helper.suggest_optimizations(query)
    return render(request, 'suggest.html', {'results': response[0].text})
