from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .forms import PostForm
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-timestamp']

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