from django.shortcuts import render, get_object_or_404
from . import models


# TODO: transfer the templates

def posts_list(request):
    posts = models.Post.objects.all().order_by('-createDate')
    # for post in posts:
    #     print(post.createDate.minute)
    context = {
        "short_description": "Learning",
        "posts": posts,
    }
    return render(request, 'post/posts_list.html', context)


def post_detail(request, post_id, slug):
    latest_posts = models.Post.objects.all().order_by('-createDate')[:5]
    post = get_object_or_404(models.Post, id=post_id, slug=slug)
    categories = models.Post.objects.filter(category__post_categories__title__icontains=post.title)
    context = {
        "post": post,
        "latest_posts": latest_posts,
        "categories": categories,
    }
    return render(request, 'post/posts_detail.html', context)
