# Generated by Django 4.0.2 on 2022-03-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_image_remove_blog_url_blog_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(),
        ),
    ]