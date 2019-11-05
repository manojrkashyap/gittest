# Generated by Django 2.0 on 2019-11-04 06:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('action', models.CharField(db_column='action', max_length=255)),
                ('audit_datetime', models.DateTimeField(db_column='audit_date_time', default=django.utils.timezone.now)),
                ('performed_by', models.CharField(db_column='performed_by', default=None, max_length=255)),
                ('message', models.TextField(db_column='message')),
                ('audit_details', models.TextField(db_column='audit_details')),
            ],
            options={
                'verbose_name_plural': 'audits',
            },
        ),
    ]