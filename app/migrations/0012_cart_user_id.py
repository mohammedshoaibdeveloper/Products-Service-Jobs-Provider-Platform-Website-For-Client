# Generated by Django 3.0.1 on 2020-03-02 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_cart_sno'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.User_Signup'),
            preserve_default=False,
        ),
    ]
