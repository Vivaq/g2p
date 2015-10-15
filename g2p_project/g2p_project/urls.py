from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from g2p_project.views import logout_page

urlpatterns = patterns(
    '',
    (r'^', include('g2p.urls')),
    (r'^logout/$', logout_page),
    url(r'^login/', 'django.contrib.auth.views.login'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)