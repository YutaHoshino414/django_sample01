from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Category


def Index(request):
    #posts = Post.objects.all().order_by('id')
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    posts = Post.objects.filter(category__name__icontains=q)

    categories = Category.objects.all()

    context = {'posts': posts, 'categories':categories}
    return render(request, 'blogs/post_list.html', context)

def Detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blogs/post_detail.html', {'post': post})