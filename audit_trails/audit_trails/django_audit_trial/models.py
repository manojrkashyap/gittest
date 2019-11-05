from django.db import models
from django.utils import timezone

# Create your models here.

class Audit(models.Model):
    class Meta:
        verbose_name_plural = "audits"

    action = models.CharField(max_length=255, db_column='action')
    audit_datetime = models.DateTimeField(default=timezone.now, db_column='audit_date_time')
    performed_by = models.CharField(default=None, db_column="performed_by", max_length=255)
    message = models.TextField(db_column='message')
    audit_details = models.TextField(db_column='audit_details')

    def __str__(self):
        return self.action
