# Generated by Django 3.1.2 on 2020-10-14 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201014_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.departamento'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='myapp.Habilidad'),
        ),
    ]
