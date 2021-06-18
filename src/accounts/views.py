# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# App
from .forms import SignUpForm
from .models import Profile
from .filters import ProfileFilter
# 3rd party
import json
from django_filters.views import FilterView

from django.views.generic import ListView


class ProfileListView(LoginRequiredMixin, FilterView):
    """
    Retrieves profiles marked as public and
    ordered by amount of comments received
    """
    model = Profile 
    template_name = 'profiles/profile_list.html'
    paginate_by = 10
    filterset_class = ProfileFilter

    def get_queryset(self):
        query = self.model.objects.filter(user__is_staff=False, is_public=True) \
                    .prefetch_related('instruments') \
                    .annotate(num_comments=Count('comments_received')) \
                    .annotate(num_experiences=Count('experiences')) \
                    .order_by('-num_comments', '-num_experiences')
        return query

    
class ProfileDetailView(LoginRequiredMixin, DetailView):

    model = Profile 
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'

def Login(request):

    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        # stayloggedin = request.GET.get('stayloggedin')
        # if stayloggedin == "true":
        #  pass
        # else:
        #  request.session.set_expiry(0)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(json.dumps({"message": "Success"}),content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message": "inactive"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "invalid"}),content_type="application/json")

    else:
	    return HttpResponse(json.dumps({"message": "denied"}),content_type="application/json")

def SignUp(request):
    if request.user.is_authenticated:
	    return redirect('/')

    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_group = request.POST.get('is_group')
        data = {'first_name':fname, 'last_name':lname, 'email':email, 'password2':password2, 'password1':password1, 'is_group': is_group}
        form = SignUpForm(data=data)
        if form.is_valid():
            user = form.save(commit=False)
            if user.is_group:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
            return HttpResponse(json.dumps({"message": "Success"}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message":form.errors}),content_type="application/json")
    else:
            form = SignUpForm()
