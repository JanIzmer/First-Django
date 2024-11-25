from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

def is_superuser(user):
    return user.is_superuser

class NewsDetailView(DetailView):
    model = Articles
    template_name= "news/detail_view.html"
    context_object_name = 'article'

@method_decorator(login_required, name='dispatch')
class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm
    def get_queryset(self):
        # Only allow users to edit their own posts
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(author=self.request.user)

    def form_valid(self, form):
        # If the user is not the author, deny access
        if form.instance.author != self.request.user and self.request.user.is_superuser==False:
            return HttpResponseForbidden("You are not allowed to edit this post.")
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news-delete.html'
    success_url= '/news'
    def get_queryset(self):
        # Only allow users to edit their own posts
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(author=self.request.user)
        
    def get_object(self, queryset=None):
        # Get the object to delete and make sure it's the author's own post
        obj = super().get_object(queryset)
        if obj.author != self.request.user and self.request.user.is_superuser==False:
            raise HttpResponseForbidden("You are not allowed to delete this post.")
        return obj


def news_home(request):
    news = Articles.objects.order_by('dete')
    return render(request, 'news/news_home.html', {'news': news})

@login_required
def create(request):
    error=''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            my_object = form.save(commit=False)
            my_object.author = request.user  # Set author to the logged-in user
            my_object.save()
            return redirect('/news')
        else:
            error = 'Form is not valid'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)
# Create your views here.
