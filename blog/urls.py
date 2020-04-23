from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('post-create/', views.PostCreate, name='post-create'),
    path('delete_post/<post_id>', views.PostDelete, name='delete-post'),
    path('update-post/<post_id>/', views.UpdatePost, name='update-post'),
    path('post/<post_id>/', views.PostDetailView, name='detail-view'),
    path('about/', views.about, name="blog-about"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)