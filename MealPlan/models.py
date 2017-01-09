from django.db import models

class User(models.Model):
	name = models.CharField(max_length=200)

class MealPlan(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=200, null=True)
	calories = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	protein = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	carbs = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	fat = models.DecimalField(max_digits=10, decimal_places=3, null=True)

class Meal(models.Model):
	mealPlan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=200, null=True)
	calories = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	protein = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	carbs = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	fat = models.DecimalField(max_digits=10, decimal_places=3, null=True)

class Food(models.Model):
	meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=200, null=True)
	calories = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	protein = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	carbs = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	fat = models.DecimalField(max_digits=10, decimal_places=3, null=True)
	GI = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)







