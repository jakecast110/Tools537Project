from django.db import models
from accounts.models import CustomUser

class Survey(models.Model):
	Survey_name = models.CharField(max_length=200)
	Survey_description = models.CharField(max_length=200)
	State = models.CharField(max_length=20)
	Time_created = models.DateTimeField(auto_now=True)
	Creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Questions(models.Model):
	Question_description = models.CharField(max_length=200)
	Question_type = models.CharField(max_length=10)
	Survey_from = models.ForeignKey(Survey, on_delete=models.CASCADE)


class Answers(models.Model):
	Answer = models.CharField(max_length=200)
	Question = models.ForeignKey(Questions, on_delete=models.CASCADE)
	Survey_for = models.ForeignKey(Survey, on_delete=models.CASCADE)
