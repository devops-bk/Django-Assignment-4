from django.shortcuts import render
from django.http import HttpResponseNotFound
from datetime import date
from .models import Author,Post,Comment,Tag
from .forms import PostForm


def get_date(post):
    return post['date']

def index_page(request):
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
    selected_post = Post.objects.get(slug=post_slug)
    post_tags = selected_post.tags.all()
    if selected_post:
        return render(request, "artBlog/post_detail.html", {
            "post": selected_post,
            "post_tags": post_tags
        })
    else:
        return HttpResponseNotFound("Post Not Found")

def LogIn(request):
    form = PostForm()
    if request.method == 'POST':
        return render(request,"artBlog/login.html",{
            'forms':form
        })
    return render(request,'artBlog/login.html',{
        'forms':form
    })