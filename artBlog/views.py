from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView, DetailView, ListView
from .models import Post,Comment
from .forms import PostForm, CommentForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.sessions.models import Session


class AddPost(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        form = PostForm()
        return render(request, "artBlog/addpost.html", {
            "forms": form
        })

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "artBlog/thanks.html")
        return render(request, 'artBlog/addpost.html', {
            'forms': form
        })

class CommentView(LoginRequiredMixin,View):
    login_url = "login"
    def get(self,request):
        comment = CommentForm()
        return render(request, 'artBlog/commentform.html',
        {
            'forms': comment
        })

    def post(self, request):
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment.save()
            return render(request, "artBlog/thanks.html")
        comment = CommentForm()
        return render(request, "artBlog/commentform.html", {
            "forms": comment
        })


class index_page(View):
    def get(self, request):
        latest_posts = Post.objects.all().order_by("-date")[:3]
        return render(request, "artBlog/index.html", {
            "posts": latest_posts
        })

def posts(request):
    all_posts = Post.objects.all()
    return render(request, "artBlog/all_posts.html", {
        "posts": all_posts
    })

def post_detail(request, post_slug):
    selected_post = Post.objects.get(slug = post_slug)
    if selected_post:
        comment = Comment.objects.all()
        comments = comment[len(comment)::-1]
        if post_slug in request.session:
            f_session = request.session[post_slug]
        else:
            f_session = False
        return render(request, "artBlog/post_detail.html", {
            "posts": selected_post,
            "comments": comments,
            "favoritepost": f_session
        })
    else:
        return HttpResponseNotFound("Post Not Found")


class AddFavorite(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request):

        f_slug = request.POST['slug']
        request.session[f_slug] = f_slug
        url = reverse("selected-post", kwargs={'post_slug': f_slug})
        return HttpResponseRedirect(url)


class FavoritePost(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "artBlog/favourite.html", {
            "posts": posts
        })