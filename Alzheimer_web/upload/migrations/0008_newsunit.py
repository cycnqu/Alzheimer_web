# Generated by Django 4.0.3 on 2022-05-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_upload_image_predict_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoid', models.CharField(max_length=10)),
                ('nickname', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('pubtime', models.DateTimeField(auto_now=True)),
                ('press', models.IntegerField(default=0)),
            ],
        ),
    ]
