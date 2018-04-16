from django.db import models

# Create your models here.

class Indicator(models.Model):

	id 				= models.AutoField(max_length = 5, primary_key = True)
	indicator_id 	= models.CharField(max_length = 255)
	title 			= models.CharField(max_length = 255)
	description 	= models.TextField(blank = True)
	created_at 		= models.DateTimeField(auto_now_add=True, null=True)
	updated_at 		= models.DateTimeField(auto_now=True, null=True)


	def __str__(self): # Value that we see in DJANGO ADMIN
		return self.title + " - " + self.indicator_id

	class Meta:
		db_table = "indicators" # Table name in DB