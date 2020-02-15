from django.urls import reverse_lazy, path
from django.views.generic import CreateView, TemplateView

from .models import Post


class HomePageView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'pages/home.html'

    def get_success_url(self):
        return reverse_lazy("home", args=[])  


    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        self.object = post.save()
        return super().form_valid(post)


class PostListingView(TemplateView):

    template_name = 'pages/post-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context