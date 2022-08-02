from django.shortcuts import render, get_object_or_404
from . import models


# TODO: transfer the templates

def posts_list(request):
    posts = models.Post.objects.all()
    posts_count = posts.count()
    context = {
        "posts": posts,
        "posts_count": posts_count,
    }
    return render(request, '', context)


def post_detail(request, post_id, slug):
    post = get_object_or_404(models.Post, post_id, slug)
    context = {
        "post": post,
    }
    return render(request, '', context)
