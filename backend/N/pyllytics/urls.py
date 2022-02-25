
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path(
        'descriptive/',
        views.DescriptiveStatisticsList.as_view()
    ),
    path(
        'descriptive/<str:source_pk>/',
        views.DescriptiveStatisticsDetail.as_view()
    ),
    path(
        'correlation/',
        views.CorrelationList.as_view()
    ),
    path(
        'correlation/<str:source_pk>/',
        views.CorrelationDetail.as_view()
    ),
    path(
        'source_types/',
        views.SourceTypesList.as_view()
    ),
    path(
        'source_types/<str:source_pk>/',
        views.SourceTypesDetail.as_view()
    )
]

