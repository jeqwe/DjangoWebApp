from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseGone, HttpResponseServerError

# Create your views here.
from main.forms import AddNewsForm
from main.models import News, UserLikes


def index(request):
    post = News.objects.first()
    context = {
        'last_post': post
    }
    return render(request, 'main/index.html', context)


def get_news_by_slug(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)
    context = {
        'post': post,
    }
    if request.user.is_authenticated:
        user_likes = UserLikes.objects.filter(user=request.user, post=post)
        context['likes'] = user_likes
    return render(request, 'main/post.html', context)


def get_news_by_id(request, post_id):
    post = get_object_or_404(News, pk=post_id)
    context = {
        'post': post,
    }
    if request.user.is_authenticated:
        user_likes = UserLikes.objects.filter(user=request.user, post=post)
        context['likes'] = user_likes
    return render(request, 'main/post.html', context)


def news(request):
    posts = News.objects.filter(moderated=True)
    context = {
        'posts': posts,
    }
    if request.user.is_authenticated:
        user_likes = UserLikes.objects.filter(user=request.user)
        context['likes'] = user_likes
    return render(request, 'main/news.html', context)


def add_news(request):
    context = {}
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            form.save()
            context['status'] = True
        else:
            context['status'] = False

    else:
        form = AddNewsForm()
        context['form'] = form
    return render(request, 'main/addnews.html', context)


def about(request):
    return render(request, 'main/about.html')


def error_410(request):
    return render(request, '410.html', status=410)


def set_like(request, post_id):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    if request.POST:
        raise PermissionDenied()
    post = get_object_or_404(News, id=post_id)
    user = get_object_or_404(User, id=request.user.id)
    user_likes = UserLikes.objects.filter(user=user, post=post)
    if user_likes.count() > 0:
        post.likes_count -= 1
        user_likes.delete()
    else:
        like = UserLikes.objects.create(user=user, post=post)
        post.likes_count += 1
    post.save()
    return redirect('news')


def login(request):
    form = LoginView()
    return render(request, 'main/../templates/registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        username = form.cleaned_data.get('username')
        return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})
