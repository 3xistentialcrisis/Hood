from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'hoodapp'

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
