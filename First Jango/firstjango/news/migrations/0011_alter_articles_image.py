# Generated by Django 5.0.4 on 2024-11-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, default='pythonlogo.webp', upload_to='images'),
        ),
    ]