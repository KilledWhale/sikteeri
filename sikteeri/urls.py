from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sikteeri/', include('sikteeri.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^static/membership/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEMBERSHIP_STATIC_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^membership/', include('membership.urls')),
    url(r'^services/', include('services.urls')),

    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    url(r'^', 'sikteeri.views.frontpage', name='frontpage'),
    # url(r'^', 'django.views.generic.simple.direct_to_template', {'template': 'frontpage.html'}, name='frontpage'),
)
