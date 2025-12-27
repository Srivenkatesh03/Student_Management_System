from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Student
import os

@receiver(post_delete, sender=Student)
def delete_student_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)