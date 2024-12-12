from django.db import models
from Users.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='projects_created' 
        )
    members = models.ManyToManyField(
        User, 
        blank=True, 
        related_name='member_projects'  # Пользователи, участвующие в проекте
        )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
