from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^$', views.post_sale_list, name='post_sale_list'),
    url(r'^(?P<pk>\d+)/$', views.post_sale_detail, name = 'post_sale_detail' ),
    url(r'^new/$', views.post_sale_new, name = 'post_sale_new'),
]