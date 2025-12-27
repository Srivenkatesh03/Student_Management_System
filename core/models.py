from django.db import models
from django.core.validators import MinValueValidator

class Student(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
        ('EEE', 'Electrical'),
        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    year = models.IntegerField()
    image = models.ImageField(upload_to='students/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name