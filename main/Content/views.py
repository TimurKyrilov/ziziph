from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import request
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import PostsForm
from .models import Posts
from people.models import Profile


def main_page(request):
    posts = Posts.objects.all()
    return render(request, 'Content/main_page.html', {'posts': posts})

def page_404(request, exception):
    return render(request, 'Content/404.html', {'path': request.path}, status=404)

def redirecting_page(request):
    return redirect('/home/')

class PostsCreateView(CreateView):
    model = Posts
    form_class = PostsForm
    template_name = 'Content/create_post.html'
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)