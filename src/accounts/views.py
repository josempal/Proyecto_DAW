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
# 3rd party
import json

class ProfileListView(LoginRequiredMixin, ListView):
    """
    Retrieves profiles marked as public and
    ordered by amount of comments received
    """
    model = Profile 
    template_name = 'profiles/profile_list.html'
    
    """ queryset = Profile.objects.filter(is_public=True) \
                    .prefetch_related('instruments') \
                    .annotate(num_comments=Count('comments_received')) \
                    .annotate(num_experiences=Count('experiences')) \
                    .order_by('-num_comments', '-num_experiences') """

    def get_queryset(self):
        query = self.model.objects.exclude(user__is_staff=True, id=self.request.user.id)
        return query
class ProfileDetailView(LoginRequiredMixin, DetailView):

    model = Profile 
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'
""" class SignupView(View):
    Users sign up view

    template_name = 'registration/register.html'
    form_class = SignupForm
    success_message = 'Registro completado. Ahora puede iniciar sesión.'
    success_url = reverse_lazy('index') """



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
		data = {'first_name':fname, 'last_name':lname, 'email':email, 'password2':password2, 'password1':password1}
		form = SignUpForm(data=data)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = True
			user.save()
			return HttpResponse(json.dumps({"message": "Success"}),content_type="application/json")
		else:
			return HttpResponse(json.dumps({"message":form.errors}),content_type="application/json")
	else:
		form = SignUpForm()
	return HttpResponse(json.dumps({"message": "Denied"}),content_type="application/json")
	# return render(request, 'registration/signup.html', {'form':form})