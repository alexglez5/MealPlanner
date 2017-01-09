from django.shortcuts import render
from django.http import Http404

from MealPlan.models import Food, Meal, MealPlan, User

def home(request):
	foods = Food.objects.all()
	breakfast = Meal.objects.create()
	return render(request, 'MealPlan/home.html', {
		'foods': foods,
	})
