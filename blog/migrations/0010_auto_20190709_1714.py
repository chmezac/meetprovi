# Generated by Django 2.2.3 on 2019-07-09 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190709_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='tipo_lugar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Tipo_Lugar'),
        ),
    ]
