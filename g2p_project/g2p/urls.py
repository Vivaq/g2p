from django.conf.urls import patterns, url

urlpatterns = patterns(
    'g2p.views',
    url(r'^downloadData/$', 'downloadData', name='downloadData'),
)
