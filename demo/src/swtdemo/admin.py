from django.contrib import admin

from swtdemo.models import Concern, Employee


class ConcernAdmin(admin.ModelAdmin):
    pass
admin.site.register(Concern, ConcernAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Employee, EmployeeAdmin)
