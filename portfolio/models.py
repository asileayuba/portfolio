from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=100, default="Asile Ayuba")
    profile_image = CloudinaryField("image")

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Asile Ayuba")
    profile_image = CloudinaryField("image")  # Replaces ImageField
    resume = models.FileField(upload_to="resumes/")  
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title} - {self.company}"
    
    
class Education(models.Model):
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"
    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    progress = models.PositiveIntegerField(help_text="Skill proficiency in percentage (1-100)")
    
    def __str__(self):
        return f"{self.name} ({self.progress})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=225)
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    image = CloudinaryField("image", blank=True, null=True)  # Replaces ImageField
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"