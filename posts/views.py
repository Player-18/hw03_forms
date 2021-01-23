from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewForm
from .models import Group, Post, User


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    return render(request, "group.html", {"group": group, "posts": posts})


def new_post(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username=request.user)
            post.save()
            return redirect('index')
        return render(request, 'new.html', {'form':form})
    form = NewForm()
    return render(request, 'new.html', {'form':form})
