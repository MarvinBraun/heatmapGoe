from django.db import models


# Model CarRental

class Carstation (models.Model):

	#models.field -> Database mappuing
	name = models.CharField(max_length=40)
	lengtitude = models.DecimalField(decimal_places=10, max_digits=10000)
	longtitude = models.DecimalField(decimal_places=10, max_digits=10000)
	address = models.CharField(max_length=40)
	bookings = models.IntegerField(default=0)
