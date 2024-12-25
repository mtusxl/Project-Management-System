from django.db import models
from Projects.models import Project

class Dashbord(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    total_task = models.PositiveIntegerField(default=0)
    completed_task = models.PositiveIntegerField(default=0)
    pending_task = models.PositiveIntegerField(default=0)
