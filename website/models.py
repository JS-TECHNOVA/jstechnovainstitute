from django.db import models
from datetime import datetime


def upload_tutor_iamge(instance, filename):
    year = datetime.now().strftime("%Y")
    return f"tutors/{year}/{filename}"
# Create your models here.
class Tutors(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to= upload_tutor_iamge, null=True, blank=True)
    qualification = models.CharField(max_length=100)
    year_of_exp = models.PositiveSmallIntegerField()
    subject = models.CharField(max_length=150)

    date_of_joining = models.DateField(blank=True, null=True)
    about = models.CharField(max_length=100)

    def __str__(self):
        return self.name
   

def upload_student_feedback(instance, filename):
    year = datetime.now().strftime("%Y")
    return f'student_feedback/{year}/{instance.country}/{filename}'

class StudentFeedbacks(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_student_feedback)

    def __str__(self):
        return self.name