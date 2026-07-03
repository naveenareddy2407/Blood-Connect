from django.contrib import admin
from . models import patient,donardetail

@admin.register(patient)
class Adminpatient(admin.ModelAdmin):
    list_display=['id','Full_Name','Phone']
@admin.register(donardetail)
class Admindonars(admin.ModelAdmin):
    list_display=['id','Full_Name','Phone']

