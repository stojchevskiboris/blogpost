from django.urls import path
from . import views
from .models import Post
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.index, name='home'),
    path('add/post/', views.add, name='add'),
    path('profile/', views.profile, name='profile'),
    path('blockedUsers/', views.blockedUsers, name='blockedUsers'),
    path("<int:post_id>/", views.detail, name="detail"),
    path("<int:post_id>/delete/", views.deletePost, name="deletePost"),
    path("<int:post_id>/<int:postComment_id>/delete/", views.deleteComment, name="deleteComment"),
    path("<int:post_id>/edit/", views.editPost, name="editPost"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.loginView, name="loginView"),
    path("logout/", views.logoutView, name="logoutView"),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
