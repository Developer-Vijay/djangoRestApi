# Generated by Django 4.2.1 on 2023-05-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_employee_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='experience',
            field=models.CharField(default='1', max_length=100),
        ),
    ]