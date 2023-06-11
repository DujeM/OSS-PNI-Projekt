from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('None', {'fields':('role', 'status')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('None', {'fields':('role', 'status')}),
    )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ('name', 'code', 'program', 'ects', 'sem_red', 'sem_izv', 'optional', 'owner')
    list_display = ('name', 'code', 'ects', 'owner')
