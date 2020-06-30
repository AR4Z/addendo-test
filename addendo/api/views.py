from .models import Consultant, Organization
from rest_framework import viewsets
from .serializers import ConsultantSerializer, OrganizationSerializer

class ConsultantViewSet(viewsets.ModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer