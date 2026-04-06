from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'socialnetworks'

router = routers.SimpleRouter()
router.register('', views.SocialNetworkViewSet, basename='socialnetworks')

urlpatterns = [
    path('', include(router.urls) )
]