# Generated by Django 5.1.5 on 2025-01-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('action_time', models.DateTimeField()),
                ('is_error', models.BooleanField(default=False)),
                ('is_success', models.BooleanField(default=False)),
                ('error_message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]