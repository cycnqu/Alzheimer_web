# Generated by Django 4.0.3 on 2022-05-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_alter_upload_image_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_image',
            name='predict_tag',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
