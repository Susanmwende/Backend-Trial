
from django.db import models
from user.models import User

# Create your models here.

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=50, default="AkiraChix")
    email = models.EmailField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming User with ID 1 exists
    def __str__(self):
        return f"{self.school_name} {self.email}"
