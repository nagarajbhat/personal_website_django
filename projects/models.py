from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=140)
	small_desc = models.CharField(max_length=1000)
	desc = models.TextField()
	tech_used = models.TextField()
	tryit = models.CharField(max_length=1000,null=True,blank=True)
	source_code = models.CharField(max_length=1000,null=True,blank=True)
	
	date = models.DateTimeField()

	def __unicode__(self):
		return self.title