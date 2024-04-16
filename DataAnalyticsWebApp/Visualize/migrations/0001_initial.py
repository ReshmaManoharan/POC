# Generated by Django 4.2.11 on 2024-04-15 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'country',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'industry',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('founded', models.IntegerField()),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Visualize.industry')),
                ('no_of_employees', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Visualize.country')),
            ],
            options={
                'verbose_name': 'organization',
            },
        ),
    ]
