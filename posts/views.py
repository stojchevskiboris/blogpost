from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "index.html", context)


def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {"form": form}
    return render(request, 'add.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "detail.html", context)
