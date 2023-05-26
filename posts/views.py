from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, PostComment
from .forms import PostForm, CommentForm


# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "index.html", context)


def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # ToDo: Fix no image bug
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {"form": form}
    return render(request, 'add.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = PostComment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = request.user
            comment.post = post
            form.save()
            return redirect('detail', post_id)
    else:
        form = CommentForm()

    context = {"post": post, "form": form, "comments": comments}
    return render(request, "detail.html", context)


def deletePost(request, post_id):
    posts = Post.objects.all()
    post = posts.filter(pk=post_id)
    post.delete()
    return redirect('home')


def deleteComment(request, post_id, postComment_id):
    comments = PostComment.objects.all()
    comment = comments.filter(pk = postComment_id)
    print(comments)
    comment.delete()
    return redirect('detail',post_id)
