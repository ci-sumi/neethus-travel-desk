# Generated by Django 5.1 on 2024-09-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('best_time_to_visit', models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Spring', 'Spring'), ('Winter', 'Winter')], default='Spring', max_length=6)),
                ('budget_type', models.CharField(choices=[('Budget', 'Budget'), ('Mid-range', 'Mid-range'), ('Luxury', 'Luxury')], default='Mid-range', max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='destinations/')),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
