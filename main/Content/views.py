from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .forms import PostsForm
from .models import Posts

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
    
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostsDetailView(DetailView):
    model = Posts
    template_name = "Content/Posts_detail.html"
