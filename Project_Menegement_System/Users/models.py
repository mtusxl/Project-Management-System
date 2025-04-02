from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser): 
    projects = models.ManyToManyField(
        "Projects.Project", 
        blank=True, 
        related_name='users'
    )
    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk:  # Только при создании нового пользователя
            self.set_password(self.password)  # Хэшируем пароль
        super().save(*args, **kwargs)
