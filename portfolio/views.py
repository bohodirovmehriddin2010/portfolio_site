from django.shortcuts import render
from .models import About, Education, Experience, Blog, Links, Contact

def home(request):
    portfolio = About.objects.all()
    context = {
        'portfolio': portfolio
    }
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def single_portfolio(request):
    return render(request, 'single_portfolio.html')