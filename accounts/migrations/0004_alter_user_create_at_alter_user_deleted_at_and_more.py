# Generated by Django 4.2.4 on 2023-09-05 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_create_at_user_deleted_at_user_is_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_at'),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='deleted_at'),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='update_at'),
        ),
    ]
