# Generated by Django 4.2.13 on 2025-01-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descr', models.TextField()),
                ('image', models.ImageField(upload_to='slider/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Slider Item',
                'verbose_name_plural': 'Slider Items',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='main_slider_name_700476_idx'), models.Index(fields=['-created_at'], name='main_slider_created_0531eb_idx')],
            },
        ),
    ]
