from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.Signup, name='register'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name="logout"),
    path('video/', views.video_list, name="video_list"),
    # path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)