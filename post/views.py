from django.views.generic import ListView, DetailView
from .models import Post, PostComment


class PostsListView(ListView):
    template_name = 'post/posts_list.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-updateDate', ]
    paginate_by = 3

    def get_queryset(self):
        query_set = super(PostsListView, self).get_queryset()
        return query_set.filter(isActive=True).order_by('-createDate')


class PostDetailView(DetailView):
    template_name = 'post/posts_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        query_set = super(PostDetailView, self).get_context_data()
        post: Post = kwargs.get('object')
        query_set['latest_posts'] = Post.objects.all().order_by('-createDate')[:5]
        query_set['comments'] = PostComment.objects.filter(indicated_post_id=post.id, parent=None).prefetch_related('postcomment_set')
        return query_set

    def get_queryset(self):
        query = super(PostDetailView, self).get_queryset()
        return query.filter(isActive=True)
