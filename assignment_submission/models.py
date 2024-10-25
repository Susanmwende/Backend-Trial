# Create your models here.
from django.db import models
from student.models import Student
from assignments.models import Assignments

class AssignmentSubmissionManager(models.Manager):
    def count_completion_status(self):
        return {
            "completed": self.filter(completion_status=True).count(),
            "not_completed": self.filter(completion_status=False).count(),
        }

class AssignmentSubmission(models.Model):
    submission_id = models.AutoField(primary_key=True)  # Ensure this is the primary key
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    submitted_date = models.DateTimeField(auto_now_add=True)
    completion_status = models.BooleanField(default=False)
    image_upload = models.FileField(upload_to='images/', blank=True) 

    # Add the custom manager
    objects = AssignmentSubmissionManager()

    def __str__(self):
        return f"Submission {self.submission_id} - Grade: {self.grade}"

    @classmethod
    def count_submissions(cls, assignment_id):
        """Count the number of submissions for a specific assignment."""
        return cls.objects.filter(assignment_id=assignment_id).count()




          {
      id: 'agriculture',
      title: 'Agriculture',
      icon: '🌾',
      icons: [
        '🚜', '🌻', '👨‍🌾', '🐄', '🍎', '🥕', '🌽', '🐑', '🐓', '🍇',
        '🍞', '🌿', '🍠', '🧄', '🧅', '🍒', '🍓', '🥭', '🥥', '🍋',
        '🍉', '🍊', '🍍', '🥬', '🥒', '🧑‍🌾', '🍑', '🌸', '🌷', '🥔'
      ],
    },
    {
      id: 'modeling',
      title: 'Modeling (Clay)',
      icon: '🏺',
      icons: [
        '🎨', '🖌️', '🧱', '🖼️', '🧑‍🎨', '🧑‍🏭', '🎭', '👩‍🎨', '🧑‍🎤', '🎬',
        '🖍️', '🖊️', '🧶', '🧵', '📐', '📏', '🎴', '✂️', '🧩', '🖼️',
        '🎭', '🧑‍🎨', '🎨', '🖌️', '🎨', '🧑‍🏭', '🎭', '🧩', '🖍️', '📐'
      ],
    },
    {
      id: 'environment',
      title: 'Environment',
      icon: '🌍',
      icons: [
        '🌱', '🍃', '🌳', '♻️', '💧', '🌤', '🌊', '🏞', '🦜', '🌿',
        '🌵', '🍂', '🌾', '🏔', '🌋', '🍄', '🦋', '🪲', '🐝', '🐛',
        '🐞', '🦚', '🌸', '🌷', '🍀', '🐾', '🐦', '🦥', '🍁', '🦥'
      ],
    },
    {
      id: 'art_and_craft',
      title: 'Art and Craft',
      icon: '✂️',
      icons: [
        '✂️', '🧵', '🖍️', '🧷', '🧩', '📏', '🖊️', '📐', '🖌️', '🧶',
        '🧑‍🎨', '🎨', '🎭', '🎬', '🎨', '🧑‍🏭', '🧩', '📏', '📐', '🎴',
        '📎', '📓', '🖇', '📖', '🧵', '🖼', '🖍', '🎭', '🧷', '📚'
      ],
    },
    {
      id: 'knitting',
      title: 'Knitting',
      icon: '🧶',
      icons: [
        '🧣', '🧷', '👕', '🧤', '🧢', '🧦', '🧵', '👒', '👗', '👚',
        '🧥', '👔', '👘', '🧤', '🧵', '🧷', '🧣', '🧦', '🧑‍🎨', '🧥',
        '🧑‍🎨', '🧤', '🧣', '🧶', '✂️', '📏', '🧑‍🎨', '📐', '📎', '🧵'
      ],
    },
    {
      id: 'cooking',
      title: 'Cooking',
      icon: '🍳',
      icons: [
        '🍔', '🥘', '🍕', '🍜', '🍱', '🍝', '🥗', '🍲', '🍰', '🍣',
        '🍤', '🍩', '🥞', '🍴', '🍇', '🍧', '🍮', '🍫', '🍿', '🥐',
        '🍔', '🍟', '🍖', '🍗', '🥓', '🍞', '🍍', '🍤', '🔪', '🍴', '🥄', 
        '🍽', '🧂', '🍶', '🍯', '🍶', '🥢', '🍚', '🫖', '🍵'
      ],
    },