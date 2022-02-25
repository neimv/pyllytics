from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from pyllytics.models import (
        DescriptiveStatisticsModel,
        CorrelationModel,
        SourceTypesModel
    )
from pyllytics.serializers import (
        DescriptiveStatisticsSerializer,
        CorrelationSerializer,
        SourceTypesSerializer
    )


def index(request):
    return HttpResponse("hello")


class DescriptiveStatisticsList(APIView):
    def get(self, request, format=None):
        ds = DescriptiveStatisticsModel.objects.all()
        serializer = DescriptiveStatisticsSerializer(ds, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DescriptiveStatisticsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DescriptiveStatisticsDetail(APIView):
    def _get_object(self, source_pk):
        try:
            return DescriptiveStatisticsModel.objects.get(source=source_pk)
        except DescriptiveStatisticsModel.DoesNotExist:
            raise Http404

    def get(self, request, source_pk, format=None):
        ds = self._get_object(source_pk)
        serializer = DescriptiveStatisticsSerializer(ds)

        return Response(serializer.data)

    def put(self, request, source_pk, format=None):
        ds = self._get_object(source_pk)
        serializer = DescriptiveStatisticsSerializer(ds)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, source_pk, format=None):
        ds = self._get_object(source_pk)
        ds.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CorrelationList(APIView):
    def get(self, request, format=None):
        ds = CorrelationModel.objects.all()
        serializer = CorrelationSerializer(ds, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CorrelationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CorrelationDetail(APIView):
    def _get_object(self, source_pk):
        try:
            return CorrelationModel.objects.get(source=source_pk)
        except CorrelationModel.DoesNotExist:
            raise Http404

    def get(self, request, source_pk, format=None):
        ds = self._get_object(source_pk)
        serializer = CorrelationSerializer(ds)

        return Response(serializer.data)

    def put(self, request, source_pk, format=None):
        ds = self._get_object(source_pk)
        serializer = CorrelationSerializer(ds)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, source_pk, format=None):
        ds = self._get_object(source_pk)
        ds.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class SourceTypesList(APIView):
    def get(self, request, format=None):
        ds = SourceTypesModel.objects.all()
        serializer = SourceTypesSerializer(ds, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SourceTypesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SourceTypesDetail(APIView):
    def _get_object(self, source_pk):
        try:
            return SourceTypesModel.objects.get(source=source_pk)
        except SourceTypesModel.DoesNotExist:
            raise Http404

    def get(self, request, source_pk, format=None):
        ds = self._get_object(source_pk)
        serializer = SourceTypesSerializer(ds)

        return Response(serializer.data)

    def put(self, request, source_pk, format=None):
        ds = self._get_object(source_pk)
        serializer = SourceTypesSerializer(ds)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, source_pk, format=None):
        ds = self._get_object(source_pk)
        ds.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
