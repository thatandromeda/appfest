from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

urlpatterns += patterns(
    'appfest.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^open/$', 'open', name='open'),
    url(r'^question/(?P<question_id>\d+)/(?P<question_text>\w*)/$', 'question', name='question'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)