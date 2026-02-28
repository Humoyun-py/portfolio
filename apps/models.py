from django.db import models

class Project(models.Model):
    img_url = models.URLField(max_length=255)
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField()  # Proficiency level (e.g., 1-100)
    
    def __str__(self):
        return self.name
    
