from django.db import models
from accounts.models import User

from datetime import datetime,time

class Assessment(models.Model):

    LANGUAGE_CHOIES=[
            ("python","python"),
            ("java","java"),
            ("c","c")
        ]

    STATUS_CHOICES=[
        ("draft","draft"),
        ("scheduled","scheduled"),
        ("in progress","in progress"),
        ("completed","completed"),
    ]

    
    title=models.CharField(max_length=200)
    batch=models.CharField(max_length=200)
    language=models.CharField(max_length=200,choices=LANGUAGE_CHOIES)
    exam_date=models.DateField()
    duration=models.DurationField()
    start_time=models.TimeField()
    end_time=models.TimeField(null=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=200,choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        end_datetime=datetime.combine(self.exam_date,self.start_time)+self.duration
        self.end_time=end_datetime.time()

        return super().save(*args,**kwargs)
    