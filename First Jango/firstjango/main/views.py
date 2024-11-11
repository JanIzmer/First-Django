from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from news.forms import RegisterForm
from django.urls import reverse_lazy, reverse
# Create your views here.
def index (request):
    return render(request, 'main/index.html', {'title': 'Page about python'})
def about (request):
    return render(request, 'main/about.html')
@login_required
def profile_view(request):
    return render(request, 'main/profile.html')
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)