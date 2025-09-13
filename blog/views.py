from django.shortcuts import render
from django.views import View
from .models import Post

class BlogListView(View):
    template_name = 'blog/blog_list.html'

    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')  # جدیدترین‌ها اول
        context = {
            'posts': posts
        }
        return render(request, self.template_name, context)
