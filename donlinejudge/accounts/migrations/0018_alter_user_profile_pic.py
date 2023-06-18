# Generated by Django 3.2.2 on 2021-06-13 08:58

from django.db import migrations, models
import utils.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210610_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar/__default__.png', null=True, upload_to=utils.file_upload.FileUploadUtils._wrapper),
        ),
    ]