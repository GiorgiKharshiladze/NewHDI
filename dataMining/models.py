from django.db import models

# Create your models here.

class Indicator(models.Model):

	def __str__(self): # Value that we see in DJANGO ADMIN
		return str(self.my_id) + ": " + str(self.name) 

	class Meta:
		db_table = 'indicators'

	id = models.AutoField(primary_key=True)
	my_id = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank = True)
	source = models.CharField(max_length=255, null=True)
	proportional = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)
