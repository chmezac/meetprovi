# Generated by Django 2.2.3 on 2019-07-09 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_lugar_tipo_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='tipo_lugar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Tipo_Lugar'),
        ),
    ]
