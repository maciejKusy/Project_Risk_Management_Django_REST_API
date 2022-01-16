from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Project, Risk
from .serializers import ProjectSerializer, RiskSerializer


class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]


class RiskView(ModelViewSet):
    serializer_class = RiskSerializer
    queryset = Risk.objects.all()
    permission_classes = [IsAuthenticated]
