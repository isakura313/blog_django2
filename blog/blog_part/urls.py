from django.urls import path
from . import views
app_name = 'blog_part'
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.post_list, name='post_list'), path('<slug:post>', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)