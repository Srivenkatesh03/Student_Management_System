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

class Subject(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
        ('EEE', 'Electrical'),
        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
    ]
    name = models.CharField(max_length=100)
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES
    )
    max_marks = models.PositiveIntegerField(default=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
            return f"{self.name} ({self.get_department_display()})"

    
class Marks(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='marks'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='marks'
    )

    marks_obtained = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student','subject')

    def __str__(self):
                return f"{self.student.name} - {self.subject.name}: {self.marks_obtained}"

    
