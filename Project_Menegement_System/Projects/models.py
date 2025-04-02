from django.db import models
from django.utils.text import slugify

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
    slug = models.SlugField(max_length=255, unique=True, blank=True, allow_unicode=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Создаем slug только если его нет
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

