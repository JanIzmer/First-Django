from django.shortcuts import render,get_object_or_404
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
@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'main/profile.html', {'user': user})
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)