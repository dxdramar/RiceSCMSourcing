from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Transaksi, Metrik, AnnualData

@admin.register(Transaksi)
class TransaksiAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Transaksi._meta.get_fields()]
    
    def get_export_queryset(self, request):
            """
            Returns export queryset.
            Default implementation respects applied search and filters.
            """
            list_display = self.get_list_display(request)
            list_display_links = self.get_list_display_links(request, list_display)
            list_filter = self.get_list_filter(request)
            search_fields = self.get_search_fields(request)
            if self.get_actions(request):
                list_display = ['action_checkbox'] + list(list_display)

            ChangeList = self.get_changelist(request)
            cl = ChangeList(request, self.model, list_display,
                            list_display_links, list_filter, self.date_hierarchy,
                            search_fields, self.list_select_related, self.list_per_page,
                            self.list_max_show_all, self.list_editable, self, None
                            )

            return cl.get_queryset(request)


@admin.register(Metrik)
class MetrikAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Metrik._meta.get_fields()]
    
    def get_export_queryset(self, request):
            """
            Returns export queryset.
            Default implementation respects applied search and filters.
            """
            list_display = self.get_list_display(request)
            list_display_links = self.get_list_display_links(request, list_display)
            list_filter = self.get_list_filter(request)
            search_fields = self.get_search_fields(request)
            if self.get_actions(request):
                list_display = ['action_checkbox'] + list(list_display)

            ChangeList = self.get_changelist(request)
            cl = ChangeList(request, self.model, list_display,
                            list_display_links, list_filter, self.date_hierarchy,
                            search_fields, self.list_select_related, self.list_per_page,
                            self.list_max_show_all, self.list_editable, self, None
                            )

            return cl.get_queryset(request)    

@admin.register(AnnualData)
class AnnualDataAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in AnnualData._meta.get_fields()]
    
    def get_export_queryset(self, request):
            """
            Returns export queryset.
            Default implementation respects applied search and filters.
            """
            list_display = self.get_list_display(request)
            list_display_links = self.get_list_display_links(request, list_display)
            list_filter = self.get_list_filter(request)
            search_fields = self.get_search_fields(request)
            if self.get_actions(request):
                list_display = ['action_checkbox'] + list(list_display)

            ChangeList = self.get_changelist(request)
            cl = ChangeList(request, self.model, list_display,
                            list_display_links, list_filter, self.date_hierarchy,
                            search_fields, self.list_select_related, self.list_per_page,
                            self.list_max_show_all, self.list_editable, self, None
                            )

            return cl.get_queryset(request)    