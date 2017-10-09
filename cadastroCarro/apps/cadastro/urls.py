from django.conf.urls import url
from apps.cadastro import views

urlpatterns = [
    url('^$', views.cadastro_list, name='lista'),
]

