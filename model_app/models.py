from django.db import models

class SpecialForm(models.Model):
    name = models.CharField(max_length=255)
    roll = models.PositiveIntegerField()
    email_field = models.EmailField()
    exam_day = models.DateField()
    exam_time = models.DateTimeField()
    exam_duration = models.DurationField()
    expected_exam_finish_time = models.TimeField()
    expected_average_marks = models.DecimalField(max_digits=5, decimal_places=2)
   
    big_auto_field = models.BigAutoField(primary_key=True)  
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    message_to_us = models.TextField()

    def __str__(self):
        return self.name
