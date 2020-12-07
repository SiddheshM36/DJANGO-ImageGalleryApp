from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<int:cid>/', views.show_catergory, name='show_catergory'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)