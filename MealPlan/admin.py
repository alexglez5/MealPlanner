from django.contrib import admin

from .models import Food

class FoodAdmin(admin.ModelAdmin):
	list_display = ['title', 'calories', 'protein', 'carbs', 'fat', 'GI']

admin.site.register(Food, FoodAdmin)
