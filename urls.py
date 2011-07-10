from django.conf.urls.defaults import *
from userprofile.forms import ProfileForm
from settings import SITE_MEDIA_PATH
from views import showme

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^openid/', include('django_openid_auth.urls')),
    (url(r'^profiles/create/', 'profiles.views.create_profile', {'form_class': ProfileForm, 'template_name' : 'profiles/enter_profile.html', 'extra_context' : { 'action' : 'Create'} }, name = 'profiles_create_profile')),
    (url(r'^profiles/edit/', 'profiles.views.edit_profile', {'form_class': ProfileForm, 'template_name' : 'profiles/enter_profile.html', 'extra_context' : { 'action': 'Edit'} }, name = 'profiles_edit_profile')),
    (r'^profiles/', include('profiles.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : SITE_MEDIA_PATH}),
    (url(r'^$', showme, name = 'go_home')),
)
