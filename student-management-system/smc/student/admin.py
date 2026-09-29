from django.contrib import admin
from .models import Student, Profile

# admin.site.register(Student)

@admin.register(Student)
class StudnetAdmin(admin.ModelAdmin):
    list_display = ('name','roll','email')
    list_filter = ('name','roll')
    search_fields = ('name',)
    sortable_by = ('roll',)


# admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('department','batch','address')
    list_filter = ('department',)
    search_fields = ('department','batch')
    sortable_by = ('department','batch')