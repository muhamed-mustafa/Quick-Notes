# Generated by Django 3.1.3 on 2020-11-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201118_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='developer.jpg', upload_to='profile_img'),
        ),
    ]