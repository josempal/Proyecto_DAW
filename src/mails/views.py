# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.http import Http404
# App
from .models import Mail

class MailListView(LoginRequiredMixin, ListView):

    model = Mail
    template_name = 'mails/mails_list.html'

    def get_queryset(self):
        query = self.model.objects.filter(to_user=self.request.user)
        return query

    def get_context_data(self,**kwargs):
        context = super(MailListView,self).get_context_data(**kwargs)
        context['sent'] = self.model.objects.filter(from_user=self.request.user)
        context['total_sent'] = context['sent'].count()
        context['unread'] = self.get_queryset() \
            .filter(is_read=False)
        context['total_unread'] = self.get_queryset() \
            .filter(is_read=False).count()
        return context

class MailDetailView(LoginRequiredMixin, DetailView):

    model = Mail
    
    def get_success_url(self):
        return reverse('mails:mail-list')

    def get_queryset(self):
        query = self.model.objects.filter(Q(to_user=self.request.user) | Q(from_user=self.request.user))
        return query

    def get_object(self, queryset=None):
        obj = super(MailDetailView, self).get_object(queryset=queryset)
        if obj:
            if not obj.is_read:
                obj.is_read = True
                obj.save(update_fields=['is_read'])
            return obj
        else:
            return None

class MailDeleteView(LoginRequiredMixin, DeleteView):

    model = Mail 

    def get_success_url(self):
        return reverse('mails:mails-list')

    def get_object(self, queryset=None):
        obj = super(MailDeleteView, self).get_object()
        if not obj.to_user == self.request.user:
            raise Http404('No existe o el correo no le fue enviado a usted')
        return obj