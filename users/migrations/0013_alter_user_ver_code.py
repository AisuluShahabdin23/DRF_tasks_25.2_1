# Generated by Django 5.0 on 2023-12-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='506928033386', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
