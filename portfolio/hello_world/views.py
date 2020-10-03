from django.shortcuts import render

# Hello World application


def hello_world(request):
    return render(request, "hello_world.html", {})
