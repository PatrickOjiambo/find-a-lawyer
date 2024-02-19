from django.contrib import admin

# Register your models here.
from models import Client, Lawyer, Lawyer_practice_areas, Reviews, Roles
admin.site.register(Client)
admin.site.register(Lawyer)
admin.site.register(Lawyer_practice_areas)
admin.site.register(Reviews)
admin.site.register(Roles)
