
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest 


def index(request):
    # Construct a dictionary to pass to the template engine as its aontext.
    # Note the key bold message matches to{{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request: HttpRequest):
    return render(request, 'rango/about.html')