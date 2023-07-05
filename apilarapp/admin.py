from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title','id','subtitle','author']