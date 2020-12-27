from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ImageUploadView, CategoryUploadView, userreg, ImageDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('like/', views.like_post, name='like_post'),
    path('category/<int:cid>/', views.show_catergory, name='show_catergory'),
    path('image-upload/', ImageUploadView.as_view(), name = 'image-upload'),
    path('cat-upload/', CategoryUploadView.as_view(), name = 'cat-upload'),
    path('register/', views.userreg, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('<pk>/delete/', ImageDeleteView.as_view(), name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)