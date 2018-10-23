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
 
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) 
# 
#   # url(r'^booking/$', views.booking, name='booking'),
    # url(r'^confirmation/$', views.confirming, name='confirming'),
    # url(r'^payment/$', views.payment, name='payment'),