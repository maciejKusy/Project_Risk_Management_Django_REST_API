from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Project, Risk
from .serializers import ProjectSerializer, RiskSerializer, ProjectSerializerForUpdateRequests, \
    RiskSerializerForUpdateRequests


class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST']:
            return ProjectSerializerForUpdateRequests
        else:
            return super().get_serializer_class()


class RiskView(ModelViewSet):
    serializer_class = RiskSerializer
    queryset = Risk.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST']:
            return RiskSerializerForUpdateRequests
        else:
            return super().get_serializer_class()
