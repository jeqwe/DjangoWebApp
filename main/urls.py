from main import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('error410', views.error_410, name='error_410'),
    path('write_your_name_in_history', views.add_news, name='add_news'),
    path('news/<int:post_id>', views.get_news_by_id, name='post_by_id'),
    path('news/<slug:post_slug>', views.get_news_by_slug, name='post_by_slug'),

]


