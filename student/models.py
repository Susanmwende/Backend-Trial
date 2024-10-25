from django.db import models
from user.models import User

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # AutoField is fine as primary key
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    school_name = models.CharField(max_length=50, default="AkiraChix")
 # Assuming User with ID 1 exists    school_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student_id} {self.user_id}"
