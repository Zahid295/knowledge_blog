from rest_framework import viewsets
from .models import Post
from .forms import PostForm
from .forms import PostUpdateForm
from .serializers import PostSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# from django.contrib.auth.decorators import login_required

# functions for views

def index(request):
    
    return render(request, 'blog/index.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/create_posts.html', {'form': form})



def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostUpdateForm(instance=post)
    return render(request, 'blog/update_post.html', {'form': form})

# @login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
        return redirect('index')
    else:
        return redirect('post_detail', post_id=post.pk)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer


