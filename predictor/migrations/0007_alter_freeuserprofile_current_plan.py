# Generated by Django 5.0.7 on 2025-01-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0006_freeuserprofile_current_plan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freeuserprofile',
            name='current_plan',
            field=models.CharField(blank=True, default='No Plan', max_length=50, null=True),
        ),
    ]
