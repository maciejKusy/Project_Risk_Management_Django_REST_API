from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Risk(models.Model):
    class Background(models.TextChoices):
        FINANCE = '1', 'Finance'
        OPERATIONS = '2', 'Operations'
        STAFFING = '3', 'Staffing'

    class Priority(models.TextChoices):
        LOW = '1', 'Low'
        MEDIUM = '2', 'Medium'
        HIGH = '3', 'High'

    class Probability(models.TextChoices):
        TEN_PERCENT = '1', '10%'
        TWENTY_PERCENT = '2', '20%'
        THIRTY_PERCENT = '3', '30%'
        FORTY_PERCENT = '4', '40%'
        FIFTY_PERCENT = '5', '50%'
        SIXTY_PERCENT = '6', '60%'
        SEVENTY_PERCENT = '7', '70%'
        EIGHTY_PERCENT = '8', '80%'
        NINETY_PERCENT = '9', '90%'
        HUNDRED_PERCENT = '10', '100%'

    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='risks')
    background = models.CharField(max_length=50, choices=Background.choices)
    user_assigned = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    priority = models.CharField(max_length=10, choices=Priority.choices)
    probability_percentage = models.CharField(max_length=6, choices=Probability.choices)

    def __str__(self):
        return self.name


