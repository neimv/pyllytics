
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
    )

]
# path(
#     'descriptive_statistics',
#     views.DescriptiveStatisticsViewSet.as_view({'get': 'list'})
# )
# ]

