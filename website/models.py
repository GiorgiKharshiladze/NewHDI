from django.db import models

# Create your models here.

class Interaction(models.Model):

	def __str__(self): # Value that we see in DJANGO ADMIN
		return str(self.data) + " - " + str(self.category)

	class Meta:
		db_table = 'interactions'

	id = models.AutoField(primary_key=True)
	data = models.TextField(null=True, blank = True)
	category = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)