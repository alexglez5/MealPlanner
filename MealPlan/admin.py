from django.contrib import admin

from .models import Food, MealPlan, Meal, User

class FoodAdmin(admin.ModelAdmin):
	list_display = ['title', 'calories', 'protein', 'carbs', 'fat', 'GI']

class MealAdmin(admin.ModelAdmin):
	list_display = ['title', 'calories', 'protein', 'carbs', 'fat']

class MealPlanAdmin(admin.ModelAdmin):
	list_display = ['title', 'calories', 'protein', 'carbs', 'fat']

class UserAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Food, FoodAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(MealPlan, MealPlanAdmin)
admin.site.register(User, UserAdmin)
