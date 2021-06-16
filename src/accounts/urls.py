# Django
from django.urls import path, include
from django.contrib.auth import views as auth_views
# App
from . import views 
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name="registration/login.html",
    #                                            authentication_form=LoginForm), 
    #                                            name='login'),
    path('login/', views.Login, name='login'),
    path('signup/', views.SignUp, name='signup'),
    #path('', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profiles/', views.ProfileListView.as_view(), name='profiles-list'),
    path('profile/<slug:slug>', views.ProfileDetailView.as_view(), name='profile-detail')
]