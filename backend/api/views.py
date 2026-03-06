"""API views for tasks."""

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """ViewSet for CRUD operations on Task objects."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, request, *args, **kwargs):
        """Delete a task and return its serialized representation."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
