# Generated by Django 3.2.7 on 2021-09-06 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bagpack', '0002_bagpack_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bagpackitem',
            name='bagpack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='bagpack.bagpack'),
        ),
    ]
