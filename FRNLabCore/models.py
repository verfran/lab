from django.db import models

class Patient(models.Model):
	firstName = models.CharField(max_length=30)
	secondName = models.CharField(max_length=30, null = True, blank=True)

	GENDER_CHOICE = (
		('M', 'Male'),
		('F', 'Female'),
		)
	gender = models.CharField(max_length=1,choices = GENDER_CHOICE, default = 'M')
	dateOfBirth = models.DateField(null=True, blank=True)
	notes = models.TextField(blank=True, null = True)
	phoneNumber = models.CharField(max_length=15,blank=True, null=True)
	email = models.EmailField(max_length=50,blank=True, null=True)

	def __str__(self):
		name = self.firstName
		if self.secondName:
			name = name + " " + self.secondName
		return name


 
