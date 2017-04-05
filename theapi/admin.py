from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from theapi.models import HistorialSMS, CuentaTwilio, Telefono


class HistorialSMSAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'destinatario', 'mensaje', 'user',)
    list_filter = ('fecha', 'destinatario', 'user', )
    readonly_fields = ('fecha', 'destinatario', 'mensaje', 'user',)

    ordering = ['-fecha', ]


class CuentaTwilioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'account', 'token', )


class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('telefono', 'cuenta')

admin.site.register(HistorialSMS, HistorialSMSAdmin)
admin.site.register(CuentaTwilio, CuentaTwilioAdmin)
admin.site.register(Telefono, TelefonoAdmin)
admin.site.unregister(Group)
