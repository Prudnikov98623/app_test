from django.http import HttpResponse
from django.shortcuts import render

def  index(request):
    context = {
        'title': 'Home',
        'content': 'Page content home',
        'list': ['one', 'two', 'three'],
        'dict': {'key': 'value'},
        'is_auth': False
    }
    return render(request, 'main/index.html', context)


def  about(request):
    return HttpResponse("Hello, world. You're at the main about.")