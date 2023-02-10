from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    response= requests.get('https://jsonplaceholder.typicode.com/users').json()
    return render(request, 'index.html', {'response':response})

