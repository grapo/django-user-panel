from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from django.contrib.auth import get_user_model, REDIRECT_FIELD_NAME

from debug_toolbar.panels import Panel

from . import views
from .forms import UserForm


class UserPanel(Panel):
    title = _("Users")
    template = 'user_panel/user_panel.html'

    @property
    def nav_subtitle(self):
        if self.toolbar.request.user.is_authenticated():
            return self.toolbar.request.user
        else:
            return _('Not authenticated')

    @classmethod
    def get_urls(cls):
        return [
            url(r'^login/(?P<pk>\d+)/', views.login_pk, name='user_panel_login_pk'),
            url(r'^login/$', views.login_credentials, name='user_panel_login_credentials'),
            url(r'^logout/$', views.logout, name='user_panel_logout'),
        ]

    def generate_stats(self, request, response):
        current = []
        User = get_user_model()
        redirect_to = request.GET.get(REDIRECT_FIELD_NAME, '')

        if request.user.is_authenticated():
            for field in User._meta.fields:
                current.append(
                    (field.attname, getattr(request.user, field.attname)))
        self.record_stats({
            'form': UserForm(),
            'next': redirect_to,
            'users': User.objects.order_by('-last_login')[:10],
            'current': current})
