# Generated by Django 2.1.1 on 2018-10-10 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0006_auto_20181010_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaksi',
            old_name='waktu_recieving',
            new_name='waktu_receiving',
        ),
    ]