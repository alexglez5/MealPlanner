from django.shortcuts import render
from django.http import Http404

from MealPlan.models import Food

def home(request):
	foods = Food.objects.exclude(calories=200)
	return render(request, 'MealPlan/home.html', {
		'foods': foods,
	})