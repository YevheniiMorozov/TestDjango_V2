from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment
from .forms import NewsForm, UserRegisterForm, UserLoginForm, CommentForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    news = News.objects.order_by("-date_create")
    comments = Comment.objects.all()
    context = {
        "news": news,
        "title": "EugeneNews",
        "comments": comments,
    }
    return render(request, "new/index.html", context)


def log(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "new/login.html", {"form": form})


def reg(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Success!")
            return redirect('home')
        else:
            messages.error(request, "Error!")
    else:
        form = UserRegisterForm()
    return render(request, "new/register.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def add_post(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = NewsForm()
        return render(request, "new/add_post.html", {'form': form})


@login_required
def view_and_add_comments(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    comments = Comment.news_item.all()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        context = {
            "news": news_item,
            "comments": comments,
            'comment_form': comment_form
        }
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            comments.user = request.user
            new_comment.post = news_item
            new_comment.save()
            return render(request, "comments.html", context)
        else:
            comment_form = CommentForm()
            return render(request, "comments.html", context)
