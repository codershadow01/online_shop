# Generated by Django 2.2.24 on 2021-10-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_category_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='category/default2.jpg', upload_to='category/'),
        ),
    ]
