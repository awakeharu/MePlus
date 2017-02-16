from django.conf.urls import url

urlpatterns = [
    url(r'^login', login, name='login'),
    # url(r'^logout', logout, name ='logout', {'next_page' : 'base.index'}),
]