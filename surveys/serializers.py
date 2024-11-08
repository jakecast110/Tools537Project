from rest_framework import serializers
from .models import Survey
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    surveys = serializers.PrimaryKeyRelatedField(many=True, queryset=Survey.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'surveys']


class SurveySerializer(serializers.ModelSerializer):
    Creator = serializers.ReadOnlyField(source='Creator.username')
    
    class Meta:
        model = Survey
        fields = ['Survey_name', 'Survey_description', 'State', 'Time_created', 'Creator']