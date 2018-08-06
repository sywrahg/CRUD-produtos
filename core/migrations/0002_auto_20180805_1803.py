# Generated by Django 2.0 on 2018-08-05 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categorys', to='core.Department'),
            preserve_default=False,
        ),
    ]