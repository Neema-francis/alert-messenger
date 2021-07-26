# Generated by Django 3.2.5 on 2021-07-25 15:44

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
            name='AlertNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_msg', models.TextField()),
                ('created_by', models.DateTimeField(auto_now_add=True)),
                ('alert_status', models.CharField(choices=[('danger', 'Danger'), ('success', 'Success'), ('info', 'Info'), ('warning', 'Warning')], default='info', max_length=10)),
                ('is_sent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
