# Generated by Django 3.0.3 on 2021-04-21 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.CharField(default='', max_length=20)),
                ('branch', models.CharField(default='', max_length=20)),
                ('year', models.CharField(default='', max_length=20)),
                ('contactno', models.CharField(default='', max_length=20)),
                ('user_image', models.URLField(null=True)),
                ('designation', models.CharField(default='', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LostItem',
            fields=[
                ('lostitemID', models.AutoField(primary_key=True, serialize=False)),
                ('lost_image', models.URLField(null=True)),
                ('title', models.CharField(max_length=2000)),
                ('author', models.CharField(default='', max_length=20)),
                ('description', models.CharField(default='', max_length=2000)),
                ('lost_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('UserID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemData',
            fields=[
                ('UID', models.CharField(default='', max_length=15)),
                ('ItemID', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=150, null=True)),
                ('Location', models.CharField(default='', max_length=100)),
                ('item_image', models.URLField(null=True)),
                ('author', models.CharField(default='', max_length=15)),
                ('Find_Date', models.DateTimeField(auto_now=True)),
                ('company', models.CharField(default='Not available', max_length=30)),
                ('color', models.CharField(max_length=10, null=True)),
                ('amount', models.BigIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('UserID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
