from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # list_display = ('title', 'description', 'date')
    # list_filter = ('date',)
    # search_fields = ('title', 'description')
    # ordering = ['date']
admin.site.register(models.Notes, PostAdmin)