from django.contrib import admin
from .models import Todo

# admin.site.register(Todo)
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')
    search_fields = ('title', 'description')
    list_filter = ('status',)
    
    


