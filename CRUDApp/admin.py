from django.contrib import admin

# Register your models here.

from CRUDApp.models import Employee

# 1. add model in admin views
# admin.site.register(Employee)

# 2. add Model in admin Views by decorater and Model Admin
# @admin.register(Employee) 
# class EmployeeAdmin(admin.ModelAdmin):
#     pass


# 3. add Model in admin Views by function  and Model Admin
# class EmployeeAdmin(admin.ModelAdmin):
#     pass          
# admin.site.register(Employee, EmployeeAdmin)


#List Views
# @admin.register(Employee) 
# class Employee2Admin(admin.ModelAdmin):
#     #fields = ('name', 'email', 'contact')              
#     fields = (('name', 'email'), 'contact')          # name    email   \n contact









# @admin.register(Employee) 
# class Employee2Admin(admin.ModelAdmin):
#     exclude = ('name','email',)      

# table views
# @admin.register(Employee) 
# class Employee2Admin(admin.ModelAdmin):
#     list_display = ('name', 'email')          

#filter
@admin.register(Employee) 
class Employee2Admin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
