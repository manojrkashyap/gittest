from django.contrib import admin
from .models import Audit


# Register your models here.


class AuditAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False


admin.site.register(Audit)
