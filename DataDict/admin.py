from django.contrib import admin
from DataDict.models import Dict,Item
# Register your models here.

class ItemInline(admin.StackedInline):
    model = Item

class DictAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(Dict,DictAdmin)
admin.site.register(Item)
