# Generated by Django 2.2.24 on 2023-06-28 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complain_flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaining_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Кто оставил жалобу'),
        ),
    ]
