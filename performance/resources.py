from import_export import resources
from .models import Transaksi

class TransaksiResource(resources.ModelResource):
    class Meta:
        model = Transaksi