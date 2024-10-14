# Create your views here.
from django.shortcuts import get_object_or_404, render

from .models import Blog


def blog_list(request):
    blogs = Blog.objects.filter(status='published').order_by('-timestamp')
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id, status='published')
    return render(request, 'blog_detail.html', {'blog': blog})
