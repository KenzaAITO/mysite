from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def my_view(request):
    return render(request, 'my_template.html')
