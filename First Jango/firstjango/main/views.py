from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def index (request):
    return render(request, 'main/index.html', {'title': 'Page about python'})
def about (request):
    return render(request, 'main/about.html')
@login_required
def profile_view(request):
    return render(request, 'main/profile.html')