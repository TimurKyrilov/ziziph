from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from .forms import PostsForm
from .models import Posts

def main_page(request):
    return render(request, 'Content/main_page.html')

def page_404(request, exception):
    return render(request, 'Content/404.html', {'path': request.path}, status=404)

def redirecting_page(request):
    return redirect('/home/')

@method_decorator(login_required, name='dispatch')
class PostsCreateView(CreateView):
    model = Posts
    form_class = PostsForm
    template_name = 'Content/create_post.html'
    success_url = reverse_lazy('Content:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)