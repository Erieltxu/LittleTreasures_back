from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Child


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'date_of_birth', 'user')