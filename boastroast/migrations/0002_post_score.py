# Generated by Django 3.0.1 on 2020-01-02 06:30

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boastroast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='score',
            field=computed_property.fields.ComputedIntegerField(compute_from='get_score', default=0, editable=False),
            preserve_default=False,
        ),
    ]
