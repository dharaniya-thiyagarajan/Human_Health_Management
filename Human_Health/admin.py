from django.contrib import admin
from .models import sleep
# Register your models here.
admin.site.register(sleep)
from .models import Food

admin.site.register(Food)

