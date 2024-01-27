from django.shortcuts import render, redirect
from django.http import request

def main_page(request):
    return render(request, 'Content/main_page.html')

def page_404(request, exception):
    return render(request, 'Content/404.html', {'path': request.path}, status=404)

def redirecting_page(request):
    return redirect('/home/')