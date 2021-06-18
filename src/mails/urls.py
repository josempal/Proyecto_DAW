# Django
from django.urls import path
# App
from . import views

app_name = 'mails'

urlpatterns = [
    path('mails/', views.MailListView.as_view(), name='mails-list'),
    path('mail/<int:pk>/', views.MailDetailView.as_view(), name="mail-detail"),
    path('mail/delete/<int:pk>/', views.MailDeleteView.as_view(), name="delete")
]