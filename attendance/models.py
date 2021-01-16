from django.db import models

# Create your models here.

class Student (models.Model):
    # GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('NA', 'I do not wish to say')]

    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    phone = models.CharField(max_length= 13, blank=True)
    address = models.CharField(max_length=200, blank=True)
    # gender = models.CharField(max_length=25, choices=GENDER_CHOICES, blank= True)

    parent_first_name = models.CharField(max_length= 200, blank=True)
    parent_last_name = models.CharField(max_length= 200, blank=True)

    contact_email = models.EmailField(max_length= 200, blank=True)

    def __str__(self):
        display = (self.first_name + " " + self.last_name)
        return display
