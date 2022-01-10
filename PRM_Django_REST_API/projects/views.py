from rest_framework.viewsets import ModelViewSet
from .models import Project, Risk
from .serializers import ProjectSerializer, DetailedRiskSerializer


class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class RiskView(ModelViewSet):
    serializer_class = DetailedRiskSerializer
    queryset = Risk.objects.all()
