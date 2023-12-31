from main import views
from django.urls import path
from django.conf.urls import handler404

handler404 = 'main.views.error_404'

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('write_your_name_in_history', views.add_news, name='add_news'),
    path('news/<int:post_id>', views.get_news_by_id, name='post_by_id'),
    path('news/<slug:post_slug>', views.get_news_by_slug, name='post_by_slug'),

]


