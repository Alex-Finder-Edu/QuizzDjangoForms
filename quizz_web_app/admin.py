from django.contrib import admin
from .models import Domain, Subdomain, Question
# Register your models here.

admin.site.register(Domain)
admin.site.register(Subdomain)
admin.site.register(Question)
