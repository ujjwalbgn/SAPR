from django.db import models

from datetime import datetime,time,date
from attendance.utils import create_new_ref_number

# Create your models here.

class Student (models.Model):
    # GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('NA', 'I do not wish to say')]

    US_STATES = [('AL', 'Alababama'),('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'),('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]

    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    student_id = models.CharField(
        max_length=4,
        # editable=False,
        unique=True,
        default=create_new_ref_number()
    )

    parent_first_name = models.CharField(max_length=200, blank=True)
    parent_last_name = models.CharField(max_length=200, blank=True)

    contact_email = models.EmailField(max_length=200, blank=True)

    phone = models.CharField(max_length= 13, blank=True)


    address_1 = models.CharField( max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField( max_length=64, default="", blank=True)
    state = models.CharField(max_length=2,choices=US_STATES, blank= True)
    zip_code = models.CharField(max_length=5, blank= True)
    # gender = models.CharField(max_length=25, choices=GENDER_CHOICES, blank= True)



    def __str__(self):
        display = (self.first_name + " " + self.last_name)
        return display

class TimeSlot (models.Model):
    time_slot = models.TimeField()

    def __str__(self):
        return str(self.time_slot)

class Schedule (models.Model):
    DAY_Choices = [('S','Sunday'),('M','Monday'),('T','Tuesday'),('W','Wednesday'),('Th','Thursday'),('F','Friday'),('Sa','Saturday')]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.CharField(max_length=9,choices=DAY_Choices)
    time_slots = models.ForeignKey(TimeSlot, on_delete= models.DO_NOTHING)


    def __str__(self):
        display = (str(self.student) + " at " + str(self.time_slots))
        return display


class ClassAttendance(models.Model):

    CLASS_TYPE_CHOICES = [('In person', 'In person'),('Online', 'Online')]
    CLASS_QTN =[('1','1'),('2','2')]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Date_time = models.DateTimeField(default=datetime.now)
    Number_of_classes = models.CharField(max_length=1,choices=CLASS_QTN)
    Class_type = models.CharField(max_length=15,choices=CLASS_TYPE_CHOICES, default='In Person')

    def __str__(self):
        display = (str(self.student) + " on " + self.Date_time.strftime("%I:%M %p  %A, %d %B %Y "))
        return display