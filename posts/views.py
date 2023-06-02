from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, PostComment
from .forms import PostForm, CommentForm
from datetime import datetime
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import AnonymousUser, User



# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "index.html", context)


@login_required
def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {"form": form}
    return render(request, 'add.html', context)


@login_required
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


@login_required
def deletePost(request, post_id):
    posts = Post.objects.all()
    post = posts.filter(pk=post_id)
    post.delete()
    return redirect('home')


@login_required
def deleteComment(request, post_id, postComment_id):
    comments = PostComment.objects.all()
    comment = comments.filter(pk=postComment_id)
    comment.delete()
    return redirect('detail', post_id)


@login_required
def editPost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        timeCreated = post.date_created
        print(timeCreated)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post2 = form.save(commit=False)
            post2.author = request.user
            post2.date_created = post.date_created

            comments = PostComment.objects.filter(post_id=post_id)

            post.delete()

            form.save()

            # for comment in comments:
            #     comment.post_id = post2.id

            return redirect('detail', post2.id)

    else:
        form = PostForm()

    context = {"form": form, "post": post, "post_id": post_id}
    return render(request, 'edit.html', context)


@login_required
def profile(request):
    user = request.user
    context = {"user": user}
    return render(request, 'profile.html', context)


def blockedUsers(request):
    user = request.user
    profiles = User.objects.all();
    context = {"user": user, "profiles": profiles}
    return render(request, 'blockedUsers.html', context)


def loginView(request):
    return redirect('home')


def logoutView(request):
    print("test")

    user = getattr(request, "user", None)
    if not getattr(user, "is_authenticated", True):
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)
    request.session.flush()
    if hasattr(request, "user"):
        request.user = AnonymousUser()
    return redirect('home')
