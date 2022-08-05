from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . import models


class PostsListView(ListView):
    template_name = 'post/posts_list.html'
    model = models.Post
    context_object_name = 'posts'

    def get_queryset(self):
        query_set = super(PostsListView, self).get_queryset()
        return query_set.filter(isActive=True).order_by('-createDate')


class PostDetailView(DetailView):
    template_name = 'post/posts_detail.html'
    model = models.Post

    def get_context_data(self, **kwargs):
        query_set = super(PostDetailView, self).get_context_data()
        query_set['latest_posts'] = models.Post.objects.all().order_by('-createDate')[:5]
        # query_set['categories'] = models.Post.objects.filter(category__post_categories__title__icontains=)
        # print(category)
        return query_set
