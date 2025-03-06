from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pictures/', default = False, null = True)

    def __str__(self):
        return self.user.username

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField(max_length=100)
    posted_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=100)
    salary = models.IntegerField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Application(models.Model):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected")
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resumes/")
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default = PENDING)
    applied_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.job} by {self.user}"
    

