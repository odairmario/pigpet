from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from estados import views


from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = format_suffix_patterns([
    # The API URLs are now determined automatically by the router.

    url(r'^estados/$',
        views.EstadoList.as_view(),
        name='estados-list'),
    url(r'^estados/(?P<pk>[0-9]+)/$',
        views.EstadoDetail.as_view(),
        name='estados-detail'),
])

