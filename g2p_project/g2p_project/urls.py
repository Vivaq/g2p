from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    (r'^', include('g2p.urls')),
    url(r'^login/', 'django.contrib.auth.views.login'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)