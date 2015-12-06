from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	quantity = models.IntegerField(blank=False, null=False)
	type = models.CharField(max_length=120, blank=False, null=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self): #python 3.3 is __str__
		return self.name
