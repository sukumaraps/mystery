# Generated by Django 4.1.3 on 2022-11-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_employee_e_sal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_sal',
            field=models.IntegerField(default=1000),
        ),
    ]
