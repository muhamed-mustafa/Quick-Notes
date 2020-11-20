from django.contrib import admin
from .models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_filter = ['active','created','tags']
    list_display = ['title','created','active']
    search_fields = ['title','content']
    list_editable = ['active','title']
    list_display_links = None
    
admin.site.register(Note,NoteAdmin)