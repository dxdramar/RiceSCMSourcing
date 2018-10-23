from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from performance.models import Transaksi, Metrik
from django.db.models import Sum, Avg, Q, Max, Min


User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {"customers": 10})

class Sourcing(TemplateView):
    template_name = 'sourcingProcessOverview.html'

class Overview(TemplateView):
    template_name = 'sourcingPerformanceOverview.html'

class Planning(TemplateView):
    template_name = 'planningPerformance.html'

class Schedule(TemplateView):
    template_name = 'scheduleProductDeliveryPerformance.html'

class ReceiveProduct(TemplateView):
    template_name = 'receiveProductPerformance.html'

class VerifyProduct(TemplateView):
    template_name = 'verifyProductPeformance.html'

class TransferProduct(TemplateView):
    template_name = 'transferProductPerformance.html'

class SupplierPayment(TemplateView):
    template_name = 'supplierPaymentPerformance.html'

class Cost(TemplateView):
    template_name = 'costPerformance.html'

class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sourcingProcessOverview.html', {"customers": 10})

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        default_items = [100, 100, 100, 100]
        data = {
                "default": default_items,
        }
        return Response(data)

class MonthLabelsData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["08/2017", "09/2017", "10/2017", "11/2017", "12/2017", "01/2018", "02/2018", "03/2018", "04/2018", "05/2018", "06/2018", "07/2018"]
        data = {
                "labels": labels,
        }
        return Response(data)

class PerformanceLabelsData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["Reliability", "Responsiveness", "Cost", "Asset Management"]
        data = {
                "labels": labels,
        }
        return Response(data)

class ForcastAccuracy(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        value = 0.881522006
        lw = Metrik.objects.filter(id=1).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=1).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=1).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=1).values_list('smax', flat=True)[0]
        if value > smax:
            snorm = 100
        elif value < smin:
            snorm = 0
        else:
            snorm = ((value-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "value": value,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class ScheduleChange(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017, jadwal_berubah=1).count()
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017, jadwal_berubah=1).count()
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017, jadwal_berubah=1).count()
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017, jadwal_berubah=1).count()
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017, jadwal_berubah=1).count()
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018, jadwal_berubah=1).count()
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018, jadwal_berubah=1).count()
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018, jadwal_berubah=1).count()
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018, jadwal_berubah=1).count()
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018, jadwal_berubah=1).count()
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018, jadwal_berubah=1).count()
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, jadwal_berubah=1).count()
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        data = {
                "default": default_items,
                "last": m12,
        }
        return Response(data)

class ScheduleChangeLTThreeDays(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count()
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=2).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=2).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=2).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=2).values_list('smax', flat=True)[0]
        scheduleChange = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, jadwal_berubah=1).count()
        notInLT = scheduleChange - m12
        sChangeInLT = m12 / scheduleChange
        if sChangeInLT > smax:
            snorm = 100
        elif sChangeInLT < smin:
            snorm = 0
        else:
            snorm = ((sChangeInLT-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "value": sChangeInLT,
                "notinlt": notInLT,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class TargetBuy(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        target = [300, 1000, 500, 300, 0, 0, 0, 4500, 6000, 3000, 500, 3000]
        last = 3000
        data = {
                "target": target,
                "last": last,
        }
        return Response(data)


class TotalBuyData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=3).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=3).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=3).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=3).values_list('smax', flat=True)[0]
        last_target = 3000
        total_buy = m12 / last_target
        if total_buy > smax:
            snorm = 100
        elif total_buy < smin:
            snorm = 0
        else:
            snorm = ((total_buy-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        unfulfilled = 3000 - m12
        if unfulfilled < 0:
            kurang = 0
        else:
            kurang = unfulfilled
        data = {
                "default": default_items,
                "last": m12,
                "value": total_buy,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
                "unfulfilled": kurang,
        }
        return Response(data)

class TotalOrderData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017).count()
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017).count()
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017).count()
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017).count()
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017).count()
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018).count()
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018).count()
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018).count()
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018).count()
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018).count()
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018).count()
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).count()
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        data = {
                "default": default_items,
        }
        return Response(data)

class OntimeReceiving(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017, jadwal_berubah=0).count()
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017, jadwal_berubah=0).count()
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017, jadwal_berubah=0).count()
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017, jadwal_berubah=0).count()
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017, jadwal_berubah=0).count()
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018, jadwal_berubah=0).count()
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018, jadwal_berubah=0).count()
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018, jadwal_berubah=0).count()
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018, jadwal_berubah=0).count()
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018, jadwal_berubah=0).count()
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018, jadwal_berubah=0).count()
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, jadwal_berubah=0).count()
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=4).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=4).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=4).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=4).values_list('smax', flat=True)[0]
        totalOrder = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).count()
        onTime = m12 / totalOrder    
        notOnTime = totalOrder - m12
        if onTime > smax:
            snorm = 100
        elif onTime < smin:
            snorm = 0
        else:
            snorm = ((onTime-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "value": onTime,
                "notontime": notOnTime,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class CorrectPackagingData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017, correct_packaging=1).count()
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017, correct_packaging=1).count()
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017, correct_packaging=1).count()
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017, correct_packaging=1).count()
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017, correct_packaging=1).count()
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018, correct_packaging=1).count()
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018, correct_packaging=1).count()
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018, correct_packaging=1).count()
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018, correct_packaging=1).count()
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018, correct_packaging=1).count()
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018, correct_packaging=1).count()
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, correct_packaging=1).count()
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=5).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=5).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=5).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=5).values_list('smax', flat=True)[0]
        totalOrder = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).count()
        notCorrect = totalOrder - m12
        correctPackaging = m12 / totalOrder
        if correctPackaging > smax:
            snorm = 100
        elif correctPackaging < smin:
            snorm = 0
        else:
            snorm = ((correctPackaging-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "value": correctPackaging,
                "notcorrect": notCorrect,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class CorrectContentData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017, correct_content=1).count()
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017, correct_content=1).count()
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017, correct_content=1).count()
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017, correct_content=1).count()
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017, correct_content=1).count()
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018, correct_content=1).count()
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018, correct_content=1).count()
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018, correct_content=1).count()
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018, correct_content=1).count()
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018, correct_content=1).count()
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018, correct_content=1).count()
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, correct_content=1).count()
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=6).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=6).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=6).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=6).values_list('smax', flat=True)[0]
        totalOrder = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).count()
        notCorrect = totalOrder - m12
        correctContent = m12 / totalOrder
        if correctContent > smax:
            snorm = 100
        elif correctContent < smin:
            snorm = 0
        else:
            snorm = ((correctContent-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "value": correctContent,
                "notcorrect": notCorrect,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class RejectionData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017) | Q(correct_packaging=0, tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017)).count()
        m2 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017) | Q(correct_packaging=0, tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017)).count()
        m3 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017) | Q(correct_packaging=0, tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017)).count()
        m4 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017) | Q(correct_packaging=0, tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017)).count()
        m5 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017) | Q(correct_packaging=0, tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017)).count()
        m6 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018) | Q(correct_packaging=0, tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018)).count()
        m7 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018) | Q(correct_packaging=0, tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018)).count()
        m8 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018) | Q(correct_packaging=0, tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018)).count()
        m9 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018) | Q(correct_packaging=0, tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018)).count()
        m10 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018) | Q(correct_packaging=0, tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018)).count()
        m11 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018) | Q(correct_packaging=0, tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018)).count()
        m12 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018) | Q(correct_packaging=0, tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018)).count()
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=7).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=7).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=7).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=7).values_list('smax', flat=True)[0]
        totalOrder = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).count()
        correctOrder = totalOrder - m12
        rejection = m12 / totalOrder
        if rejection < smax:
            snorm = 100
        elif rejection > smin:
            snorm = 0
        else:
            snorm = ((rejection-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "correct": correctOrder,
                "value": rejection,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)


# Section

class PlanningTime(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        value = 11
        lw = Metrik.objects.filter(id=8).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=8).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=8).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=8).values_list('smax', flat=True)[0]
        if value < smax:
            snorm = 100
        elif value > smin:
            snorm = 0
        else:
            snorm = ((value-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "value": value,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class AverageDaysScheduleChange(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=9).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=9).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=9).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=9).values_list('smax', flat=True)[0]
        if m12 < smax:
            snorm = 100
        elif m12 > smin:
            snorm = 0
        else:
            snorm = ((m12-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class ReceivingTimeData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=10).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=10).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=10).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=10).values_list('smax', flat=True)[0]
        if m12 < smax:
            snorm = 100
        elif m12 > smin:
            snorm = 0
        else:
            snorm = ((m12-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class VerifyTimeData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=11).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=11).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=11).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=11).values_list('smax', flat=True)[0]
        if m12 < smax:
            snorm = 100
        elif m12 > smin:
            snorm = 0
        else:
            snorm = ((m12-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class TransferTimeData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=12).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=12).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=12).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=12).values_list('smax', flat=True)[0]
        if m12 < smax:
            snorm = 100
        elif m12 > smin:
            snorm = 0
        else:
            snorm = ((m12-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class PaymentTimeData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=13).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=13).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=13).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=13).values_list('smax', flat=True)[0]
        if m12 < smax:
            snorm = 100
        elif m12 > smin:
            snorm = 0
        else:
            snorm = ((m12-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class PurchaseOrderCycleTime(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=14).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=14).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=14).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=14).values_list('smax', flat=True)[0]
        if m12 < smax:
            snorm = 100
        elif m12 > smin:
            snorm = 0
        else:
            snorm = ((m12-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class LaborCostData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=15).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=15).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=15).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=15).values_list('smax', flat=True)[0]
        if m12 < smax:
            snorm = 100
        elif m12 > smin:
            snorm = 0
        else:
            snorm = ((m12-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)


class MaterialCostData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        m1 = Transaksi.objects.filter(tanggal_penerimaan__month=8, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m2 = Transaksi.objects.filter(tanggal_penerimaan__month=9, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m3 = Transaksi.objects.filter(tanggal_penerimaan__month=10, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m4 = Transaksi.objects.filter(tanggal_penerimaan__month=11, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m5 = Transaksi.objects.filter(tanggal_penerimaan__month=12, tanggal_penerimaan__year=2017).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m6 = Transaksi.objects.filter(tanggal_penerimaan__month=1, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m7 = Transaksi.objects.filter(tanggal_penerimaan__month=2, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m8 = Transaksi.objects.filter(tanggal_penerimaan__month=3, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m9 = Transaksi.objects.filter(tanggal_penerimaan__month=4, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m10 = Transaksi.objects.filter(tanggal_penerimaan__month=5, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m11 = Transaksi.objects.filter(tanggal_penerimaan__month=6, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        m12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        default_items = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
        lw = Metrik.objects.filter(id=16).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=16).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=16).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=16).values_list('smax', flat=True)[0]
        if m12 < smax:
            snorm = 100
        elif m12 > smin:
            snorm = 0
        else:
            snorm = ((m12-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "default": default_items,
                "last": m12,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class IDOS(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        value = 28.5
        lw = Metrik.objects.filter(id=17).values_list('lw', flat=True)[0]
        gw = Metrik.objects.filter(id=17).values_list('gw', flat=True)[0]
        smin = Metrik.objects.filter(id=17).values_list('smin', flat=True)[0]
        smax = Metrik.objects.filter(id=17).values_list('smax', flat=True)[0]
        if value < smax:
            snorm = 100
        elif value > smin:
            snorm = 0
        else:
            snorm = ((value-smin)/(smax-smin))*100
        lscore = snorm * lw
        fscore = snorm * gw
        data = {
                "value": value,
                "smin": smin,
                "smax": smax,
                "snorm": snorm,
                "lscore": lscore,
                "fscore": fscore,
        }
        return Response(data)

class Score(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        lw = Metrik.objects.all().values_list('lw', flat=True)
        gw = Metrik.objects.all().values_list('gw', flat=True)
        smin = Metrik.objects.all().values_list('smin', flat=True)
        smax = Metrik.objects.all().values_list('smax', flat=True)
        
        value0 = 0.881522006
        if value0 > smax[0]:
            snorm0 = 100
        elif value0 < smin[0]:
            snorm0 = 0
        else:
            snorm0 = ((value0-smin[0])/(smax[0]-smin[0]))*100
        lscore0 = snorm0 * lw[0]
        fscore0 = snorm0 * gw[0]
        
        scheduleChange = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, jadwal_berubah=1).count()
        last1 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, jadwal_berubah=1, jumlah_hari_berubah__lte=3).count() 
        value1 = last1 / scheduleChange
        if value1 > smax[1]:
            snorm1 = 100
        elif value1 < smin[1]:
            snorm1 = 0
        else:
            snorm1 = ((value1-smin[1])/(smax[1]-smin[1]))*100
        lscore1 = snorm1 * lw[1]
        fscore1 = snorm1 * gw[1]

        target = 3000
        last2 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Sum('jumlah_netto')).get('jumlah_netto__sum', 0.00) / 1000
        value2 = last2 / target
        if value2 > smax[2]:
            snorm2 = 100
        elif value2 < smin[2]:
            snorm2 = 0
        else:
            snorm2 = ((value2-smin[2])/(smax[2]-smin[2]))*100
        lscore2 = snorm2 * lw[2]
        fscore2 = snorm2 * gw[2]

        totalOrder = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).count()
        
        last3 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, jadwal_berubah=0).count()
        value3 = last3 / totalOrder
        if value3 > smax[3]:
            snorm3 = 100
        elif value3 < smin[3]:
            snorm3 = 0
        else:
            snorm3 = ((value3-smin[3])/(smax[3]-smin[3]))*100
        lscore3 = snorm3 * lw[3]
        fscore3 = snorm3 * gw[3]

        last4 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, correct_packaging=1).count()
        value4 = last4 / totalOrder
        if value4 > smax[4]:
            snorm4 = 100
        elif value4 < smin[4]:
            snorm4 = 0
        else:
            snorm4 = ((value4-smin[4])/(smax[4]-smin[4]))*100
        lscore4 = snorm4 * lw[4]
        fscore4 = snorm4 * gw[4]

        last5 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, correct_content=1).count()
        value5 = last5 / totalOrder
        if value5 > smax[5]:
            snorm5 = 100
        elif value5 < smin[5]:
            snorm5 = 0
        else:
            snorm5 = ((value5-smin[5])/(smax[5]-smin[5]))*100
        lscore5 = snorm5 * lw[5]
        fscore5 = snorm5 * gw[5]

        last6 = Transaksi.objects.filter(Q(correct_content=0, tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018) | Q(correct_packaging=0, tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018)).count()
        value6 = last6 / totalOrder
        if value6 < smax[6]:
            snorm6 = 100
        elif value6 > smin[6]:
            snorm6 = 0
        else:
            snorm6 = ((value6-smin[6])/(smax[6]-smin[6]))*100
        lscore6 = snorm6 * lw[6]
        fscore6 = snorm6 * gw[6]
        
        value7 = 11
        if value7 < smax[7]:
            snorm7 = 100
        elif value7 > smin[7]:
            snorm7 = 0
        else:
            snorm7 = ((value7-smin[7])/(smax[7]-smin[7]))*100
        lscore7 = snorm7 * lw[7]
        fscore7 = snorm7 * gw[7]

        value8 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018, jadwal_berubah=1).aggregate(Avg('jumlah_hari_berubah')).get('jumlah_hari_berubah__avg', 0.00)
        if value8 < smax[8]:
            snorm8 = 100
        elif value8 > smin[8]:
            snorm8 = 0
        else:
            snorm8 = ((value8-smin[8])/(smax[8]-smin[8]))*100
        lscore8 = snorm8 * lw[8]
        fscore8 = snorm8 * gw[8]

        value9 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_receiving')).get('waktu_receiving__avg', 0.00)
        if value9 < smax[9]:
            snorm9 = 100
        elif value9 > smin[9]:
            snorm9 = 0
        else:
            snorm9 = ((value9-smin[9])/(smax[9]-smin[9]))*100
        lscore9 = snorm9 * lw[9]
        fscore9 = snorm9 * gw[9]

        value10 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_verify')).get('waktu_verify__avg', 0.00)
        if value10 < smax[10]:
            snorm10 = 100
        elif value10 > smin[10]:
            snorm10 = 0
        else:
            snorm10 = ((value10-smin[10])/(smax[10]-smin[10]))*100
        lscore10 = snorm10 * lw[10]
        fscore10 = snorm10 * gw[10]

        value11 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_transfer')).get('waktu_transfer__avg', 0.00)
        if value11 < smax[11]:
            snorm11 = 100
        elif value11 > smin[11]:
            snorm11 = 0
        else:
            snorm11 = ((value11-smin[11])/(smax[11]-smin[11]))*100
        lscore11 = snorm11 * lw[11]
        fscore11 = snorm11 * gw[11]

        value12 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_payment')).get('waktu_payment__avg', 0.00)
        if value12 < smax[12]:
            snorm12 = 100
        elif value12 > smin[12]:
            snorm12 = 0
        else:
            snorm12 = ((value12-smin[12])/(smax[12]-smin[12]))*100
        lscore12 = snorm12 * lw[12]
        fscore12 = snorm12 * gw[12]

        value13 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('waktu_po')).get('waktu_po__avg', 0.00)
        if value13 < smax[13]:
            snorm13 = 100
        elif value13 > smin[13]:
            snorm13 = 0
        else:
            snorm13 = ((value13-smin[13])/(smax[13]-smin[13]))*100
        lscore13 = snorm13 * lw[13]
        fscore13 = snorm13 * gw[13]

        value14 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_pekerja')).get('biaya_pekerja__avg', 0.00)
        if value14 < smax[14]:
            snorm14 = 100
        elif value14 > smin[14]:
            snorm14 = 0
        else:
            snorm14 = ((value14-smin[14])/(smax[14]-smin[14]))*100
        lscore14 = snorm14 * lw[14]
        fscore14 = snorm14 * gw[14]

        value15 = Transaksi.objects.filter(tanggal_penerimaan__month=7, tanggal_penerimaan__year=2018).aggregate(Avg('biaya_material')).get('biaya_material__avg', 0.00)
        if value15 < smax[15]:
            snorm15 = 100
        elif value15 > smin[15]:
            snorm15 = 0
        else:
            snorm15 = ((value15-smin[15])/(smax[15]-smin[15]))*100
        lscore15 = snorm15 * lw[15]
        fscore15 = snorm15 * gw[15]

        value16 = 28.5
        if value16 < smax[16]:
            snorm16 = 100
        elif value16 > smin[16]:
            snorm16 = 0
        else:
            snorm16 = ((value16-smin[16])/(smax[16]-smin[16]))*100
        lscore16 = snorm16 * lw[16]
        fscore16 = snorm16 * gw[16]

        lreliability = lscore0 + lscore1 + lscore2 + lscore3 + lscore4 + lscore5 + lscore6 
        lresponsiveness = lscore7 + lscore8 + lscore9 + lscore10 + lscore11 + lscore12 + lscore13
        lsourcing_cost = lscore14 + lscore15
        lasset_management = lscore16
        ltotal_score = lreliability + lresponsiveness + lsourcing_cost + lasset_management

        greliability = fscore0 + fscore1 + fscore2 + fscore3 + fscore4 + fscore5 + fscore6 
        gresponsiveness = fscore7 + fscore8 + fscore9 + fscore10 + fscore11 + fscore12 + fscore13
        gsourcing_cost = fscore14 + fscore15
        gasset_management = fscore16
        gtotal_score = greliability + gresponsiveness + gsourcing_cost + gasset_management

        data = {
                "lreliability": lreliability,
                "lresponsiveness": lresponsiveness,
                "lsourcing_cost": lsourcing_cost,
                "lasset_management": lasset_management,
                "ltotal_score": ltotal_score,
                "greliability": greliability,
                "gresponsiveness": gresponsiveness,
                "gsourcing_cost": gsourcing_cost,
                "gasset_management": gasset_management,
                "gtotal_score": gtotal_score,
        }
        return Response(data)