from rest_framework import serializers

from .models import Case, CaseParameter



class CaseParameterSerialzier(serializers.ModelSerializer):
    class Meta:
        model = CaseParameter
        fields = ['value']


class CaseSerializer(serializers.ModelSerializer):
    case_parameters = CaseParameterSerialzier(many=True, read_only=True)
    class Meta:
        model = Case
        fields = '__all__'

