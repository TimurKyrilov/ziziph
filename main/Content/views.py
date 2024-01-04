from django.shortcuts import render
from django.http import request

def main_page(request):
    return render(request, 'Content/main_page.html')
