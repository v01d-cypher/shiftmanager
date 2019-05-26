from django.contrib import admin

from .models import Employee, Roster, Shift, Upload

# Register your models here.


admin.site.register(Employee)
admin.site.register(Shift)
admin.site.register(Roster)
admin.site.register(Upload)
