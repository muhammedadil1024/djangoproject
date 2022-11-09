from django.contrib import admin
from .models import Gallery, RegTable

# Register your models here.
admin.site.register(RegTable)
admin.site.register(Gallery)