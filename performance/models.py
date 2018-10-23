from django.db import models

# Create your models here.
class Transaksi(models.Model):
    jumlah_netto = models.FloatField()
    waktu_receiving = models.FloatField()
    waktu_verify = models.FloatField()
    waktu_transfer = models.FloatField()
    waktu_payment = models.FloatField()
    waktu_po = models.FloatField()
    biaya_pekerja = models.FloatField()
    biaya_material = models.FloatField()
    jadwal_berubah = models.BooleanField()
    jumlah_hari_berubah = models.FloatField(blank=0, default=0)
    correct_packaging = models.BooleanField()
    correct_content = models.BooleanField()
    tanggal_penerimaan = models.DateField()

    class Meta:
        verbose_name_plural = "Transaksi"

class Metrik(models.Model):
    metrik = models.TextField()
    lw = models.FloatField()
    gw = models.FloatField()
    smin = models.FloatField(default=0)
    smax = models.FloatField(default=0)

class AnnualData(models.Model):
    year = models.FloatField()
    total_forcasted_sourcing_target = models.FloatField()
    total_rice_product_needed = models.FloatField()
    planning_cycle_time = models.FloatField()
    total_cost_of_goods_sold_a_year = models.FloatField()
    inventory_on_hand = models.FloatField()

    class Meta:
        verbose_name_plural = "Annual Data"