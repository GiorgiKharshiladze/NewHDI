from django.db import models

# Create your models here.
class Page(models.Model):

	def __str__(self):
		return str(self.title)

	class Meta:
		db_table = 'pages'

	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	content = models.TextField(null=True, blank = True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)