from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from main.forms import AddNewsForm
from main.models import News


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
    return render(request, 'main/post.html', context)


def get_news_by_id(request, post_id):
    post = get_object_or_404(News, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'main/post.html', context)


def news(request):
    posts = News.objects.filter(moderated=True)
    context = {
        'posts': posts,
    }
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


def error_404(request, exception):
    return render(request, 'main/404.html', status=404)
