from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from cidades import views


from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = format_suffix_patterns([
    # The API URLs are now determined automatically by the router.

    url(r'^cidades/$',
        views.CidadeList.as_view(),
        name='cidades-list'),
    url(r'^cidades/(?P<pk>[0-9]+)/$',
        views.CidadeDetail.as_view(),
        name='cidades-detail'),
])

