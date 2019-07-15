#from django.http import HttpResponse
from django.shortcuts import render


def c_home(request):
    template = 'main.html'
    data = {
        'welcome_string': 'Hey there',
        'text': 'Hello World',
        'hello': 'Hey',
    }
    return render(request, template, data)


