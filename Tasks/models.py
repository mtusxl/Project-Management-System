from django.db import models
from Users.models import User
from Projects.models import Project

class Task(models.Model):
    name = models.CharField(max_length=255)
    STATUS_CHOISES = [('to_do', 'To Do'),
                      ('in_progress', 'In progress'),
                      ('done', 'Done')]
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=50, choices=STATUS_CHOISES, default='to_do')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
