# Generated by Django 4.2.4 on 2023-09-05 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_status', models.CharField(choices=[('pb', 'published'), ('rg', 'rejected')], default='pb', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_at')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='update_at')),
                ('deleted_at', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='deleted_at')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='is_deleted')),
                ('body', models.TextField(help_text='Please write caption')),
                ('image', models.ImageField(blank=True, help_text='Please upload your image', null=True, upload_to='posts')),
                ('video', models.FileField(blank=True, help_text='please upload your video', null=True, upload_to='post/video')),
                ('location', models.CharField(blank=True, help_text='You can write the location of this post', max_length=730, null=True)),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'create_model',
                'verbose_name_plural': 'create_models',
                'abstract': False,
            },
        ),
    ]
