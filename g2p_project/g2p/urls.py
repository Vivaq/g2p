from django.conf.urls import patterns, url

urlpatterns = patterns(
    'g2p.views',
    url(r'^download_data/$', 'download_data', name='download_data'),
)
