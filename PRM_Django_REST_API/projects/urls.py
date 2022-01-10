from django.urls import path, include
from rest_framework import routers
from .views import ProjectView

router = routers.DefaultRouter()
router.register(r'projects', ProjectView, basename='project-view')


urlpatterns = [
    path('', include(router.urls)),
]