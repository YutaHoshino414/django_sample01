from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post, Category
from .forms import PostCreateForm


def index(request):
    #posts = Post.objects.all().order_by('id')
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(category__name__icontains=q)
    categories = Category.objects.all()

    context = {'posts': posts, 'categories':categories}
    return render(request, 'blogs/post_list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blogs/post_detail.html', {'post': post})

def create(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'blogs/post_form.html', {'form':form})

def update(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostCreateForm(instance=post)
    if request.method == 'POST':
        form = PostCreateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'blogs/post_form.html', {'form': form})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')

    return render(request, 'blogs/post_delete.html', {'post':post})