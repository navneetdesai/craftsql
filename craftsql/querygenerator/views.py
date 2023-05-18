from django.shortcuts import render
from django.http import HttpResponse
from . import cohere_helper
from .auth import AIROPS_API
import requests


# Display last 50% records from Employee table


def index(request):
    return render(request, 'index.html')


def querypage(request):
    return render(request, 'querypage.html')


def generate(request):
    if request.method == 'POST':
        query_input = request.POST.get('query-input')
        if not query_input:
            return render(request, 'querypage.html')
        response = cohere_helper.generate_query(query_input)
        return render(request, 'querypage.html', {'results': response.generations[0].text})
    return render(request, 'querypage.html', {'results': 'No query generated yet.'})


def explain_page(request):
    return render(request, 'explainpage.html')


def explain_sql(request):
    if request.method != 'POST':
        return render(request, 'explain.html')
    query = request.POST.get('query', '')

    api_url = 'https://api.airops.com/explain-query'
    headers = {'Authorization': f'Bearer {AIROPS_API}'}
    data = {'input': {'query': query}}
    print(headers)
    response = requests.post(api_url, headers=headers, json=data)

    print(response.text)
    if response.status_code == 200:
        explanation = response.json().get('explanation')
    else:
        explanation = 'Failed to get explanation. Please try again.'

    return render(request, 'explainpage.html', {'explanation': explanation})


def fixpage(request):
    return render(request, 'fixpage.html')

def suggest(request):
    return render(request, 'suggest.html')


def fix_query(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')

        api_url = 'https://api.airops.ai/fix-query'
        headers = {
            'Authorization': f'Bearer {AIROPS_API}',
            'Content-Type': 'application/json'
        }
        data = {
            'query': query
        }
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            fixed_query = response.json().get('fixed_query', '')
            return render(request, 'fix_results.html', {'fixed_query': fixed_query})
        else:
            error_message = 'Error occurred while fixing the query.'
            return render(request, 'fix_results.html', {'error_message': error_message})

    return render(request, 'fix_query.html')


def suggest_optimization(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')

        api_url = 'https://api.airops.ai/optimize-query'
        headers = {
            'Authorization': f'Bearer {AIROPS_API}',
            'Content-Type': 'application/json'
        }
        data = {
            'query': query
        }
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            fixed_query = response.json().get('optimization_suggestions', [])
            return render(request, 'suggest.html', {'optimization_suggestions': fixed_query})
        else:
            error_message = 'Error occurred while optimizing the query.'
            return render(request, 'suggest.html', {'error_message': error_message})

    return render(request, 'suggest.html')