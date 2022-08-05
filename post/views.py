from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . import models


class PostsListView(ListView):
    template_name = 'post/posts_list.html'
    model = models.Post
    context_object_name = 'posts'

    def get_queryset(self):
        query_set = super(PostsListView, self).get_queryset()
        return query_set.filter(isActive=True).order_by('-createDate')



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
