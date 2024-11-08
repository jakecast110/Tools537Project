from django.db import models

class Survey(models.Model):
	Survey_name = models.CharField(max_length=200)
	Survey_description = models.CharField(max_length=200)
	State = models.CharField(max_length=20)
	Time_created = models.DateTimeField(auto_now=True)
	Creator = models.ForeignKey('auth.User', related_name='surveys', on_delete=models.CASCADE)
