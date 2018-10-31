from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='profiles'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.aboutus, name='aboutus'),
    url(r'^contactus/$', views.contact, name='contact'),
    url(r'^joinsafarigroups/$', views.joingroup, name='joingroup'),
    url(r'^singlegroup/(?P<id>\d+)/', views.single, name='single'),
    url(r'^excursions/$', views.excursions, name='excursions'),
    url(r'^longsafaris/$', views.longsafaris, name='longsafaris'),
    url(r'^shortsafaris/$', views.shortsafaris, name='shortsafaris'),
    url(r'^lakenaivashapackage/$', views.lakenaivasha, name='lakenaivasha'),
    url(r'^lakenakurupackage/$', views.lakenakuru, name='lakenakuru'),
    url(r'^nairobiexcursionpackage/$', views.nairobiexcursion, name='nairobiexcursion'),
    url(r'^shortsafarislakenakuru/$', views.ssfnakuru, name='ssfnakuru'),
    url(r'^shortsafarisaberdare/$', views.aberdaressf, name='aberdaressf'),
    url(r'^shortsafarisamboseli/$', views.amboselissf, name='amboselissf'), 
    url(r'^shortsafarislakenaivasha/$', views.naivashassf, name='naivashassf'), 
    url(r'^shortsafarismaasaimara/$', views.maasaimarassf, name='maasaimarassf'),
    url(r'^shortsafarissweetwaters/$', views.pajetassf, name='pajetassf'),
    url(r'^shortsafarisamboseli3days/$', views.amboselissf3, name='amboselissf3'),
    url(r'^shortsafarissweetwater3days/$', views.sweetwaterssf3, name='sweetwaterssf3'),
    url(r'^shortsafarismaasaimara3days/$', views.maasaimarassf3, name='maasaimarassf3'),
    url(r'^shortsafarisnakuru3days/$', views.nakurussf3, name='nakurussf3'),
    url(r'^shortsafarissamburu3days/$', views.samburussf3, name='samburussf3'),
    url(r'^shortsafarismaasarimaranakuru4days/$', views.maranakurussf4, name='maranakurussf4'),
    url(r'^shortsafarisamboseli5days/$', views.amboselissf5, name='amboselissf5'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) 
# 
#   # url(r'^booking/$', views.booking, name='booking'),
    # url(r'^confirmation/$', views.confirming, name='confirming'),
    # url(r'^payment/$', views.payment, name='payment'),