# Generated by Django 4.2.5 on 2024-02-22 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0004_posts_author_posts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='author',
        ),
    ]
