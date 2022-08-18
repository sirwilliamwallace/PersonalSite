from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View
from .models import Post, PostComment
from .forms import CommentForm, SearchForm



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
        comments = PostComment.objects.filter(isApproved=True,
                                              indicated_post_id=post.id,
                                              parent=None)
        query_set['comments'] = comments.order_by('-createDate').prefetch_related('parents')
        query_set['comment_form'] = CommentForm()
        return query_set

    def post(self, request, post_id, slug):
        comment_form = CommentForm(self.request.POST)
        if comment_form.is_valid():
            data = comment_form.data
            user_id = request.user.id
            parent_id = comment_form.cleaned_data.get('parentId')
            # print(parent_id)
            comment_text = data.get('comment_text')
            PostComment(indicated_post_id=post_id, parent_id=parent_id, user_id=user_id,
                        comment_text=comment_text).save()
            messages.success(self.request, "Comment successfully uploaded and is waiting for approval")
            return redirect(f"{self.request.path}#textMessage")
        else:
            messages.warning(self.request, "Something went wrong")
            return redirect(f"{self.request.path}#textMessage")

    def get_queryset(self):
        query = super(PostDetailView, self).get_queryset()
        return query.filter(isActive=True)


class SearchPostsView(View):
    def get(self, request):
        form = SearchForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            query = data.get('search')
            if query is not None:
                posts = Post.objects.filter(title__icontains=query)
                return render(request, 'post/search_results.html', {'posts': posts})
            return render(request, 'post/search_results.html', {'posts': []})
        return render(request, 'post/includes/search_component.html', {'form': form})