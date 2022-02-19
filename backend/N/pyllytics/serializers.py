
from rest_framework import serializers
from pyllytics.models import (
        DescriptiveStatisticsModel,
        CorrelationModel,
        SourceTypesModel
    )


class DescriptiveStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptiveStatisticsModel
        fields = '__all__'


class CorrelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrelationModel
        fields = '__all__'


class SourceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceTypesModel
        fields = '__all__'

