# Generated by Django 4.1.4 on 2023-01-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=100, null=True)),
                ('cphone', models.CharField(blank=True, max_length=100, null=True)),
                ('cadd', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]