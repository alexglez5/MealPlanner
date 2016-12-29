from django.db import models

class Food(models.Model):
	title = models.CharField(max_length=200)
	calories = models.DecimalField(max_digits=5, decimal_places=3)
	protein = models.DecimalField(max_digits=5, decimal_places=3)
	carbs = models.DecimalField(max_digits=5, decimal_places=3)
	fat = models.DecimalField(max_digits=5, decimal_places=3)
	GI = models.DecimalField(max_digits=5, decimal_places=3, null=True)