from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    Blogs = Blog.objects
    return render(request, 'Blogs/allblogs.html', {'Blogs':Blogs})

def detail(request, Blog_id):
    detailblog = get_object_or_404(Blog, pk=Blog_id)
    return render(request, 'Blogs/detail.html', {'Blog':detailblog})
