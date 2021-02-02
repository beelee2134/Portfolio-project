from django.shortcuts import render

from .models import Blog

def allblogs(request):
    Blogs = Blog.objects
    return render(request, 'Blogs/allblogs.html', {'Blogs':Blogs})
