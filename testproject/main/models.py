from django.db import models

class Character(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name