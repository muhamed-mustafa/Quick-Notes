from django.contrib import admin
from .models import Profile

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_filter = ['user','slug','join_date','headline']
    list_display = ['headline','join_date']
    search_fields = ['user__first_name','headline','bio']
    list_editable = ['headline']
    list_display_links = None

admin.site.register(Profile,NoteAdmin)