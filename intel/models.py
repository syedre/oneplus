from django.db import models

class Comments(models.Model):
	name = models.CharField(max_length=120)
	comnts = models.CharField(max_length=120)