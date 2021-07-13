from django.contrib import admin
from .models import register_table,state

# Register your models here.
admin.site.site_header="my website"


class stateAdmin(admin.ModelAdmin):
	list_display=('user','billno','debit','credit')
	list_filter=('user','dt')
	



admin.site.register(register_table)
admin.site.register(state,stateAdmin)

