# Generated by Django 2.2.3 on 2019-07-09 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_tipo_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='tipo_lugar',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.Tipo_Lugar'),
        ),
    ]
