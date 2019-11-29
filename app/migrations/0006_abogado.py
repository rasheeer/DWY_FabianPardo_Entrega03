# Generated by Django 2.2.6 on 2019-11-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_abogado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abogado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
            ],
        ),
    ]
