from django.db import models
from exams.models import Assessment
from accounts.models import User


class Question(models.Model):

    title=models.CharField(max_length=200)
    description=models.TextField()
    score=models.PositiveIntegerField()
    assessment=models.ForeignKey(Assessment,on_delete=models.CASCADE)
    sample_input=models.TextField()
    sample_output=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    question_no=models.PositiveIntegerField(null=True)

    def save(self,*args,**kwargs):
        last_quest_obj=Question.objects.filter(assessment=self.assessment).last()
        if last_quest_obj:
            self.question_no=last_quest_obj.question_no+1
        else:
            self.question_no=1

        return super().save(*args,**kwargs)







