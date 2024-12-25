from django.db import models
from django.conf import settings 

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        "Users.User",
        on_delete=models.CASCADE, 
        related_name='projects_created' 
        )
    members = models.ManyToManyField(
        "Users.User", 
        blank=True, 
        related_name='projects_participating'  # Пользователи, участвующие в проекте
        )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
