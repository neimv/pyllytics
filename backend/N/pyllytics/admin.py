from django.contrib import admin

from .models import (
        SourceModel,
        DescriptiveStatisticsModel,
        CorrelationModel,
        SourceTypesModel
    )


admin.site.register(SourceModel)
admin.site.register(DescriptiveStatisticsModel)
admin.site.register(CorrelationModel)
admin.site.register(SourceTypesModel)
