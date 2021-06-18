# App
from .models import Profile
# 3rd party
import django_filters

class ProfileFilter(django_filters.FilterSet):

    displayname = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Profile
        fields = ['displayname', 'instruments__name', 'user__is_group', ]