from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from userprofile import views


from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'userprofile', views.UserProfileViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls))
]

