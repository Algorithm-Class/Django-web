from django.conf.urls import url
from . import views

urlpatterns = [

    #url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^delete$', views.delete, name='delete'),
    url(r'^query$', views.query, name='query'),
    url(r'^display/$', views.display, name='display'),
    url(r'^login/$', views.get_name, name='login'),
    url(r'^name/$', views.display, name='name1'),
    #url(r'^hello/', 'myapp.views.hello', name='hello'),
]