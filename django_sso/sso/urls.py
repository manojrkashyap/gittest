from django.conf.urls import url
from . import views

app_name = 'django_saml2_auth'

urlpatterns = [
    url(r'^acs/[0-9]$', views.acs, name="acs"),
    url(r'^welcome/$', views.welcome, name="welcome"),
    url(r'^denied/$', views.denied, name="denied"),
    url(r'^default_config', views.default_config, name='default_config')
]
