import csv
from django.http import HttpResponse
from django.contrib import admin
from torii.contact.models import Contact

def export_as_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.
    """
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_as_csv.short_description = "Export Selected as CSV"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'why_contact_us', 'reason_for_contact', 'created_at')
    readonly_fields = ('created_at',)
    actions = [export_as_csv]