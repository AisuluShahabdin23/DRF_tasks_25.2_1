# Generated by Django 5.0 on 2023-12-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='764862583164', max_length=15, verbose_name='Проверочный код'),
        ),
    ]