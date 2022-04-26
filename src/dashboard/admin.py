from django.contrib import admin

from src.dashboard.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass
