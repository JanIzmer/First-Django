from django.shortcuts import render
# Create your views here.
def index (request):
    return render(request, 'main/index.html', {'title': 'Page about python'})
def about (request):
    return render(request, 'main/about.html')