"""charts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^sourcing/$', Sourcing.as_view(), name='sourcing'),
    url(r'^sourcing/overview/$', Overview.as_view(), name='overview'),
    url(r'^sourcing/planning/$', Planning.as_view(), name='planning'),
    url(r'^sourcing/schedule/$', Schedule.as_view(), name='schedule'),
    url(r'^sourcing/receive/$', ReceiveProduct.as_view(), name='receive'),
    url(r'^sourcing/verify/$', VerifyProduct.as_view(), name='verify'),
    url(r'^sourcing/transfer/$', TransferProduct.as_view(), name='transfer'),
    url(r'^sourcing/payment/$', SupplierPayment.as_view(), name='payment'),
    url(r'^sourcing/cost/$', Cost.as_view(), name='cost'),

    url(r'^api/monthlabels/$', MonthLabelsData.as_view()),

    url(r'^api/performancelabels/$', PerformanceLabelsData.as_view()),

    url(r'^api/totalorder/$', TotalOrderData.as_view()),

    url(r'^api/correctcontent/$', CorrectContentData.as_view()),
    url(r'^api/verifytime/$', VerifyTimeData.as_view()),
    url(r'^api/rejection/$', RejectionData.as_view()),

    url(r'^api/transfertime/$', TransferTimeData.as_view()),
    url(r'^api/idos/$', IDOS.as_view()),

    url(r'^api/paymenttime/$', PaymentTimeData.as_view()),
    url(r'^api/laborcost/$', LaborCostData.as_view()),
    url(r'^api/materialcost/$', MaterialCostData.as_view()),

    url(r'^api/forecastaccuracy/$', ForcastAccuracy.as_view()),
    url(r'^api/planningtime/$', PlanningTime.as_view()),

    url(r'^api/targetbuy/$', TargetBuy.as_view()),
    url(r'^api/totalbuy/$', TotalBuyData.as_view()),
    url(r'^api/correctpackaging/$', CorrectPackagingData.as_view()),
    url(r'^api/ontime/$', OntimeReceiving.as_view()),
    url(r'^api/receivingtime/$', ReceivingTimeData.as_view()),

    url(r'^api/schedulechange/$', ScheduleChange.as_view()),
    url(r'^api/schedulechangelt3d/$', ScheduleChangeLTThreeDays.as_view()),
    url(r'^api/averagesc/$', AverageDaysScheduleChange.as_view()),
    url(r'^api/potime/$', PurchaseOrderCycleTime.as_view()),

    url(r'^api/score/$', Score.as_view()),
    
    url(r'^test/$', TestView.as_view(), name='test'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^admin/', admin.site.urls),

]
