from django.urls import path
from . import views
from .models import Post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path("<int:post_id>/", views.detail, name="detail"),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
