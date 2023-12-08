# Generated by Django 5.0 on 2023-12-08 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_user_alter_course_options_alter_department_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='course',
            field=models.ForeignKey(choices=[('BCom', 'BCom'), ('BCA', 'BCA'), ('BSc', 'BSc')], on_delete=django.db.models.deletion.CASCADE, to='store.course'),
        ),
    ]