# Generated by Django 4.0.4 on 2022-05-11 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('weight', models.FloatField(default=40, verbose_name='Weight in kg')),
                ('height', models.FloatField(default=150, verbose_name='Height in cm')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
