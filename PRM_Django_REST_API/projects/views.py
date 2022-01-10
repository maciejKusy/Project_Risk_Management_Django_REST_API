from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer


class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
