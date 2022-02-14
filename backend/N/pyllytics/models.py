import uuid

from django.db import models


# In somepoint of develop is necesary create module models/{model}.py
class SourceModel(models.Model):
    FILE = 'file'
    SQL = 'sql'
    WS = 'ws'
    TYPE_SOURCE_CHOICES = [
        (FILE, 'file'),
        (SQL, 'sql_query'),
        (WS, 'web_service')
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    source_type = models.CharField(
        max_length=32,
        choices=TYPE_SOURCE_CHOICES,
        default=FILE,
        unique=True
    )
    path = models.CharField(max_length=128, blank=False)
    user = models.CharField(max_length=32, blank=True)
    password = models.CharField(max_length=32, blank=True)
    host = models.CharField(max_length=128, blank=True)
    port = models.IntegerField(blank=True, null=True)
    type_source = models.CharField(max_length=32, blank=True)
    separator = models.CharField(max_length=4, blank=True)
    status_code = models.IntegerField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)

    class Meta:
        db_table = 'pyllytics_source'


class DescriptiveStatisticsModel(models.Model):
    source = models.ForeignKey(SourceModel, on_delete=models.CASCADE)
    results = models.JSONField()

    class Meta:
        db_table = 'pyllytics_descriptive_statistics'


class CorrelationModel(models.Model):
    source = models.ForeignKey(SourceModel, on_delete=models.CASCADE)
    results = models.JSONField()
    type_correlation = models.CharField(max_length=32)

    class Meta:
        db_table = 'pyllytics_correlation'


class SourceTypesModel(models.Model):
    source = models.ForeignKey(SourceModel, on_delete=models.CASCADE)
    original_types = models.JSONField()
    proposed_types = models.JSONField()

    class Meta:
        db_table = 'pyllytics_source_types'
