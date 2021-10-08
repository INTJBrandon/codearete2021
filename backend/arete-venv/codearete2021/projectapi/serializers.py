from rest_framework import fields, serializers
from .models import Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title', 'description', 'link', 'repo')