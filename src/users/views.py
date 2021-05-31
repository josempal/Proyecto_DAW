# Django
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
# App
from .forms import SignupForm
from .models import Profile
# 3rd party
from bootstrap_modal_forms.generic import BSModalLoginView

class ProfileListView(LoginRequiredMixin, ListView):
    """
    Retrieves profiles marked as public and
    ordered by amount of comments received
    """
    model = Profile 
    template_name = 'profiles/profile_list.html'
    paginate_by = 5
    queryset = Profile.objects.filter(is_public=True) \
                    .prefetch_related('comments_received') \
                    .prefetch_related('user__experiences') \
                    .annotate(num_comments=Count('comments_received')) \
                    .annotate(num_experiences=Count('user__experiences')) \
                    .order_by('-num_comments', '-num_experiences')

class ProfileDetailView(LoginRequiredMixin, DetailView):

    model = Profile 
    template_name = 'profiles/profile.html'

class SignupView(BSModalLoginView):
    """Users sign up view."""

    template_name = 'registration/register.html'
    form_class = SignupForm
    success_message = 'Registro completado. Ahora puede iniciar sesión.'
    success_url = reverse_lazy('index')