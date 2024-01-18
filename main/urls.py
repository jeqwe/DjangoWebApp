from main import views
from django.urls import path, include
from django.conf.urls import handler404, handler500, handler403

handler404 = views.error404
handler403 = views.error403
handler500 = views.error500


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('error410', views.error_410, name='error_410'),
    path('add_like/<int:post_id>', views.set_like, name='add_like'),
    path('write_your_name_in_history', views.add_news, name='add_news'),
    path('signup', views.signup, name='signup'),
    path('news/<int:post_id>', views.get_news_by_id, name='post_by_id'),
    path('news/<slug:post_slug>', views.get_news_by_slug, name='post_by_slug'),
    path('', include('django.contrib.auth.urls')),
]


