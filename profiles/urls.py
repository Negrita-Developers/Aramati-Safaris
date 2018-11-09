from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='profiles'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.aboutus, name='aboutus'),
    url(r'^contactus/$', views.contact, name='contact'),
    url(r'^guaranteedsafaris/$', views.guaranteedsafaris, name='guaranteedsafaris'),
    url(r'^excursions/$', views.excursions, name='excursions'),
    url(r'^longsafaris/$', views.longsafaris, name='longsafaris'),
    url(r'^shortsafaris/$', views.shortsafaris, name='shortsafaris'),

    url(r'^lakenaivashapackage/$', views.lakenaivasha, name='lakenaivasha'),
    url(r'^joinlakenaivashapackage/$', views.joinlakenaivasha, name='joinlakenaivasha'),

    url(r'^lakenakurupackage/$', views.lakenakuru, name='lakenakuru'),
    url(r'^joinlakenakurupackage/$', views.joinlakenakuru, name='joinlakenakuru'),
    
    url(r'^nairobiexcursionpackage/$', views.nairobiexcursion, name='nairobiexcursion'),

    url(r'^shortsafarislakenakuru/$', views.ssfnakuru, name='ssfnakuru'),
    url(r'^joinshortsafarislakenakuru/$', views.joinssfnakuru, name='joinssfnakuru'),

    url(r'^shortsafarisaberdare/$', views.aberdaressf, name='aberdaressf'),
    url(r'^joinshortsafarisaberdare/$', views.aberdarejoinssf, name='aberdarejoinssf'),

    url(r'^shortsafarisamboseli/$', views.amboselissf, name='amboselissf'), 
    url(r'^joinshortsafarisamboseli/$', views.amboselijoinssf, name='amboselijoinssf'),

    url(r'^shortsafarislakenaivasha/$', views.naivashassf, name='naivashassf'), 
    url(r'^joinshortsafarislakenaivasha/$', views.naivashajoinssf, name='naivashajoinssf'),

    url(r'^shortsafarismaasaimara/$', views.maasaimarassf, name='maasaimarassf'),
    url(r'^joinshortsafarismaasaimara/$', views.maasaimarajoinssf, name='maasaimarajoinssf'),

    url(r'^shortsafarissweetwaters/$', views.pajetassf, name='pajetassf'),
    url(r'^joinshortsafarissweetwaters/$', views.pajetajoinssf, name='pajetajoinssf'),

    url(r'^shortsafarisamboseli3days/$', views.amboselissf3, name='amboselissf3'),
    url(r'^joinshortsafarisamboseli3days/$', views.amboselijoinssf3, name='amboselijoinssf3'),

    url(r'^shortsafarissweetwater3days/$', views.sweetwaterssf3, name='sweetwaterssf3'),
    url(r'^joinshortsafarissweetwater3days/$', views.sweetwaterjoinssf3, name='sweetwaterjoinssf3'),

    url(r'^shortsafarismaasaimara3days/$', views.maasaimarassf3, name='maasaimarassf3'),
    url(r'^joinshortsafarismaasaimara3days/$', views.maasaimarajoinssf3, name='maasaimarajoinssf3'),

    url(r'^shortsafarisnakuru3days/$', views.nakurussf3, name='nakurussf3'),
    url(r'^joinshortsafarisnakuru3days/$', views.nakurujoinssf3, name='nakurujoinssf3'),

    url(r'^shortsafarissamburu3days/$', views.samburussf3, name='samburussf3'),
    url(r'^joinshortsafarissamburu3days/$', views.samburujoinssf3, name='samburujoinssf3'),

    url(r'^shortsafarismaasarimaranakuru4days/$', views.maranakurussf4, name='maranakurussf4'),
    url(r'^joinshortsafarismaasarimaranakuru4days/$', views.maranakurujoinssf4, name='maranakurujoinssf4'),

    url(r'^shortsafarisamboseli5days/$', views.amboselissf5, name='amboselissf5'),
    url(r'^joinshortsafarisamboseli5days/$', views.amboselijoinssf5, name='amboselijoinssf5'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) 
# 
#   # url(r'^booking/$', views.booking, name='booking'),
    # url(r'^confirmation/$', views.confirming, name='confirming'),
    # url(r'^payment/$', views.payment, name='payment'),