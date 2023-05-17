from django.shortcuts import render
from django.http import HttpResponse
from . import cohere_helper

# Display last 50% records from Employee table

# Create your views here.
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
    return render(request, 'querypage.html',  {'results': 'No query generated yet.'})



