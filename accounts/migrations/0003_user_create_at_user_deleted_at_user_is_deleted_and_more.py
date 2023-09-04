# Generated by Django 4.2.4 on 2023-09-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_mobile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='create_at'),
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='deleted_at'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(default=False, editable=False, verbose_name='is_deleted'),
        ),
        migrations.AddField(
            model_name='user',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='update_at'),
        ),
    ]
