from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .forms import PostForm
from .models import Post, Comment, Like
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-timestamp']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['likes'] = Like.objects.all()

        if self.request.user.is_authenticated:
            liked_posts = Like.objects.filter(user=self.request.user).values_list('post', flat=True)
            context['liked_posts'] = liked_posts

        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:post_list')

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if Like.objects.filter(user=request.user, post=post).exists():
        Like.objects.filter(user=request.user, post=post).delete()
        liked = False
    else:
        Like.objects.create(user=request.user, post=post)
        liked = True

    response_data = {'liked': liked, 'count': post.likes.count()}

    return redirect('posts:post_list')
