from django.contrib import admin
from .models import Company, Branch, Building, Floor, Room

admin.site.register([Company, Branch, Building, Floor, Room])
