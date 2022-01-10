from django.urls import path, include
from rest_framework import routers
from .views import ProjectView, RiskView

router = routers.DefaultRouter()
router.register(r'projects', ProjectView, basename='project-view')
router.register(r'risks', RiskView, basename='risk-view')


urlpatterns = [
    path('', include(router.urls)),
]
