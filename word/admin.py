from django.contrib import admin
from word.models import Frequency
from word.models import Store

# Register your models here.
admin.site.register(Frequency)
admin.site.register(Store)