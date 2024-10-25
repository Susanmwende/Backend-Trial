from django.db import models
from student.models import Student
from teacher.models import Teacher

class QuestionAnswer(models.Model):
    question_id = models.AutoField(primary_key=True)
    content = models.TextField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_questions')
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True, related_name='teacher_answers')
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='follow_up')
    subject = models.CharField(max_length=30)
    is_question = models.BooleanField(default=True)  # Distinguish question vs. answer
    
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    
    def __str__(self):
        return f"{self.content} ({self.status})"
