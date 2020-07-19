from . import views

app_name = 'hoodapp'

urlpatterns = [
    url('^$', views.index, name='index'),
]

