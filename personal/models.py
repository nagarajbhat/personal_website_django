from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=140)
	body1 = models.TextField()
	body2 = models.TextField(blank=True,null=True)
	date = models.DateTimeField(null=True)

	def __unicode__(self):
		return self.title	