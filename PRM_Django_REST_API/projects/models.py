from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    users_assigned = models.ManyToManyField(User)


class Risk(models.Model):
    BACKGROUND_LIST: tuple = (
        ("FIN", 'Finance'),
        ("STF", "Staffing"),
        ("OP", "Operations")
    )

    PRIORITY_LEVELS: tuple = (
        ("LOW", "Low"),
        ("MED", "Medium"),
        ("HIGH", "High"),
        ("VHIGH", "Very High")
    )

    PROBABILITY_LEVELS: tuple = (
        (1, "10%"),
        (2, "20%"),
        (3, "30%"),
        (4, "40%"),
        (5, "50%"),
        (6, "60%"),
        (7, "70%"),
        (8, "80%"),
        (9, "90%"),
        (10, "100%")
    )

    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    background = models.CharField(max_length=50, choices=BACKGROUND_LIST)
    user_assigned = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    priority = models.CharField(max_length=10, choices=PRIORITY_LEVELS, default="Low")
    probability_percentage = models.CharField(max_length=4, choices=PROBABILITY_LEVELS, default="10%")



