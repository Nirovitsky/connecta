from django.shortcuts import render

def hello_world(request):
    hello_message = "Hello, World!"
    return render(request, 'base.html', {'hello_message': hello_message})

