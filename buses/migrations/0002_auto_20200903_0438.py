# Generated by Django 3.1 on 2020-09-03 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bussescompany',
            options={'verbose_name_plural': 'bus companis'},
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(db_index=True, max_length=15)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buses.bussescompany')),
            ],
        ),
    ]
