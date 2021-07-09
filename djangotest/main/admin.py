from django.contrib import admin
from .models import List, Session, Frequency, Band

# Register your models here.


admin.site.register(List)
admin.site.register(Session)
admin.site.register(Frequency)
admin.site.register(Band)
