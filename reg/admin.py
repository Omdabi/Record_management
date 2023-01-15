from django.contrib import admin
from . models import department,teacher,student

@admin.register(department)
class dapartmentAdmin(admin.ModelAdmin):
    list_display  = ['id','dept_name']


@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display  = ['id','tname','tdept_name','tdept_name_id']



@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display  = ['id','roll','sname','father_name','contact','sdept_name','sdept_name_id']