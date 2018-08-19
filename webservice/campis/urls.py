# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from grupospet import views
# from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     url(r'^grupospet/$', views.GrupoPetList.as_view()),
#     url(r'^grupospet/(?P<pk>[0-9]+)/$', views.GrupoPetDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from campis import views


from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = format_suffix_patterns([
    # The API URLs are now determined automatically by the router.

    url(r'^campis/$',
        views.CampiList.as_view(),
        name='campis-list'),
    url(r'^campis/(?P<pk>[0-9]+)/$',
        views.CampiDetail.as_view(),
        name='campis-detail'),
])

