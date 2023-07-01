from django.urls import path
from . import views
from .views import HomeTemplateView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("", HomeTemplateView.as_view(), name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile/<username>', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]