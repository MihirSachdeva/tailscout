from rest_framework import viewsets
from ..serializers import JobSerializer
from ...models import Job


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
