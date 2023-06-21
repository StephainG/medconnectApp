from django.urls import path
from . import views
from .views import HomeTemplateView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('profile/<username>', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]