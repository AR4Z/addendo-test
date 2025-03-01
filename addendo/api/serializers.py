from .models import Organization, Consultant
from rest_framework import serializers

class ConsultantSerializer(serializers.HyperlinkedModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Organization.objects.all()
    )

    class Meta:
        model = Consultant
        fields = ('id', 'url', 'name', 'birth_date', 'organization')


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    consultants = serializers.HyperlinkedRelatedField(many=True, view_name='consultant-detail', read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'url', 'name', 'description', 'consultants')


