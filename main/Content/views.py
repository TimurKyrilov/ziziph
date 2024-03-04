from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, DetailView
from .serializers import PostsSerializer
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
    
    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if request.user.username != username:
            raise Http404("У вас нет прав доступа к созданию объектов для данного пользователя.")
        return super().dispatch(request, *args, **kwargs)

        if request.user != user_profile.user:
            return render(request, 'Content/access_denied.html')

    def form_valid(self, form):  
    
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostsDetailView(DetailView):
    model = Posts
    template_name = "Content/Posts_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.object.user.username
        context['pk'] = self.object.pk
        return context

class GetView(CreateView):
    def get_api(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, pk=kwargs['pk'])
        serializer = PostsSerializer(post)
        return JsonResponse(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.get_api(request, *args, **kwargs)
