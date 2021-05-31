# django
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'users'

urlpatterns = [
    #path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.SignupView.as_view(), name='register'),
    #path('logout/', views.LogoutView.as_view(),name='logout'),
    path('registro_completado/', TemplateView.as_view(template_name='registration/registerok.html'), name='registerok'),
    path('profiles/', views.ProfileListView.as_view(), name='profiles-list'),
    path('profile/<slug:slug>', views.ProfileDetailView.as_view(), name='profile-detail')
]