# Generated by Django 3.1.4 on 2020-12-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
