from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='profiles'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.aboutus, name='aboutus'),
    url(r'^specialoffers/', views.offers, name='offers'),
    url(r'^contactus/', views.contact, name='contact'),
    url(r'^excursions/', views.excursions, name='excursions'),
    url(r'^singleexcursion/', views.singleexcur, name='singleexcur'),
] 

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)