from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'hoodapp'

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^homepage/',views.homepage, name='homepage'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^user_profile/(?P<username>\w+)', views.user_profile, name='userprofile'),
    url(r'^update_profile/(?P<username>\w+)', views.update_profile, name='update'),
    url(r'signup/', views.signup, name='signup'),
    url(r'login/$',views.login_request, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'account/', include('django.contrib.auth.urls')),
    url(r'search/', views.search_business, name='search'),
    url(r'^post/', views.new_post, name='post'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
