# Generated by Django 2.1.3 on 2018-11-19 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]