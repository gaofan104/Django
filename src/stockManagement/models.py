from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	quantity = models.IntegerField(blank=False, null=False)
	image = models.ImageField(upload_to='img/%Y/%m/%d')
	type = models.CharField(max_length=120, blank=False, null=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def admin_image(self):
		print self.image.url
		return '<img src="%s"/>' % self.image.url
	admin_image.short_description = 'Image'
	admin_image.allow_tags = True


	def __unicode__(self): #python 3.3 is __str__
		return self.name
