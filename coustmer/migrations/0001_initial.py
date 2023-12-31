# Generated by Django 4.2.6 on 2023-10-19 14:27

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
            name='TemplatesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('templatename', models.CharField(max_length=50)),
                ('templateimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='CoustmerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forpdf', models.FileField(upload_to='')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('companyname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=10)),
                ('proposalsummary', models.TextField()),
                ('projectplanning', models.TextField()),
                ('financing', models.TextField()),
                ('created_at', models.DateField()),
                ('additionalcustomsections', models.TextField()),
                ('templatesdetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coustmer.templatesname')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Title',
            },
        ),
    ]
