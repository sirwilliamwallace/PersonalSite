from django.shortcuts import render, get_object_or_404
from . import models


# TODO: transfer the templates

def posts_list(request):
    posts = models.Post.objects.all().order_by('-updateDate')[:3]
    context = {
        "short_description": "Learning",
        "posts": posts,
    }
    return render(request, 'post/posts_list.html', context)


def post_detail(request, post_id, slug):
    post = get_object_or_404(models.Post, post_id, slug)
    context = {
        "post": post,
    }
    return render(request, 'post/posts_detail.html', context)
