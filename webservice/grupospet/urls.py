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
from grupospet import views


from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = format_suffix_patterns([
    # The API URLs are now determined automatically by the router.

    url(r'^grupospet/$',
        views.GrupoPetList.as_view(),
        name='grupospet-list'),
    url(r'^grupospet/(?P<pk>[0-9]+)/$',
        views.GrupoPetDetail.as_view(),
        name='grupospet-detail'),
])

