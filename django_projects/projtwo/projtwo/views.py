from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    my_dict = {'insert_me':'Hello from views.py!',
               'help_link':'http://127.0.0.1:8000/help',
               'help_link_text':'Help page'
               }
    return render(request, 'index.html', context=my_dict)

def help(request):
    context = {'help_text': "Help Page"}
    return render(request, 'help.html', context)