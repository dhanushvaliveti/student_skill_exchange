from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Skill, Request, Transaction

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Request)
admin.site.register(Transaction)