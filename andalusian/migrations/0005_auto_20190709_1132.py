# Generated by Django 2.1.7 on 2019-07-09 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('andalusian', '0006_auto_20190709_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumentalias',
            name='instrument',
        ),
        migrations.AlterModelManagers(
            name='instrument',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='mbid',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrument',
            name='percussion',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='InstrumentAlias',
        ),
    ]
