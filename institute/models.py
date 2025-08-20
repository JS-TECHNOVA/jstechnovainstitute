from django.db import models
from datetime import datetime


def upload_tutor_iamge(instance, filename):
    year = datetime.now().strftime("%Y")
    return f"tutors/{year}/{filename}"
# # Create your models here.
class Tutors(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to= upload_tutor_iamge, null=True, blank=True)
    qualification = models.CharField(max_length=100)
    year_of_exp = models.PositiveSmallIntegerField()
    subject = models.CharField(max_length=150)

    date_of_joining = models.DateField(blank=True, null=True)
    about = models.CharField(max_length=200)

    def __str__(self):
        return self.name
   

def upload_student_feedback(instance, filename):
    year = datetime.now().strftime("%Y")
    return f'student_feedback/{year}/{instance.country}/{filename}'

class StudentFeedbacks(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_student_feedback)

    def __str__(self):
        return self.name
    



class GetInTouch(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class DemoClassBooking(models.Model):
    booked_at = models.DateTimeField(auto_now_add=True)
    parent_phone = models.CharField(max_length=20)
    parent_email = models.EmailField()
    child_name = models.CharField(max_length=100)
    child_grade = models.CharField(max_length=10)
    board = models.CharField(max_length=30)
    subjects = models.CharField(max_length=150)

    def __str__(self):
        return self.child_name
    



def upload_tutor_cv(instance, filename):
    year = datetime.now().strftime("%Y")
    return f'tutor_cv/{year}/{filename}'

class TutorRegistrations(models.Model):
    registered_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    highest_qualification = models.CharField(max_length=50)
    subject_applying_for = models.CharField(max_length=100, null=True, blank=True)
    languages_known = models.CharField(max_length=100)
    cv = models.FileField(upload_to=upload_tutor_cv)

    def __str__(self):
        return self.name