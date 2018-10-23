# Generated by Django 2.1.1 on 2018-09-28 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaksi',
            options={'verbose_name_plural': 'Transaksi'},
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='jumlah_hari_berubah',
            field=models.FloatField(blank=0, default=0),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='tanggal_penerimaan',
            field=models.DateField(),
        ),
    ]