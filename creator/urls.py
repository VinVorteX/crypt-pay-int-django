from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'creator'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='creator/login.html'), name='login'),
    path('creators/', views.creators, name='creators'),
    path('edit/', views.edit, name='edit'),
]