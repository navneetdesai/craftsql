from django.shortcuts import render
from django.http import HttpResponse
import cohere
from . import auth

co = cohere.Client(auth.COHERE_API)


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
        print(query_input)
        response = co.generate(
            model='command-light',
            prompt=f'{query_input}\n',
            max_tokens=1032,
            temperature=0,
            k=0,
            stop_sequences=[],
            return_likelihoods='NONE')
        return render(request, 'querypage.html', {'results': response.generations[0].text[3:-3]})
    return render(request, 'querypage.html',  {'results': 'No query generated yet.'})
