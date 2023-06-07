from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    # path('logout', auth_views.LogoutView.as_view(template_name='authenticate/logout.html'), name='logout'),
    # path('login', auth_views.LoginView.as_view(template_name='authenticate/login.html'), name='login'),
]
