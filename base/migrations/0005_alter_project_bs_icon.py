# Generated by Django 3.2.3 on 2022-07-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_project_bs_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='bs_icon',
            field=models.CharField(choices=[('fas fa-headset', 'headset icon'), ('fas fa-briefcase', 'briefcase icon')], default='fas fa-headset', max_length=30),
        ),
    ]
