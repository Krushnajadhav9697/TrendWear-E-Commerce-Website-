from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','full_name','email','street','state','city','pin_code']

admin.site.register(Profile,ProfileAdmin)

