# Generated by Django 3.1 on 2020-08-23 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20200823_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='userid',
        ),
        migrations.AddField(
            model_name='order',
            name='User_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user_signup'),
        ),
    ]
