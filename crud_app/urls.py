from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^saves$',views.saves, name='saves'),
    url(r'^show_edit/(?P<id>\d+)$',views.show_edit, name='show_edit'),
    url(r'^show_edit/update/(?P<id>\d+)$',views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete')
    
]
