from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.mail import send_mail

class User(AbstractUser):

    phone=models.CharField(max_length=12,unique=True)

    ROLE_CHOICES=[
        ("admin","admin"),
        ("student","student"),
    ]

    role=models.CharField(max_length=200,choices=ROLE_CHOICES,default="student")

class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passoutyear = models.CharField(max_length=20,null=True)

    githuburl = models.URLField(null=True)

    linkedurl = models.URLField(null=True)

    student=models.OneToOneField(User,on_delete=models.CASCADE)


from django.db.models.signals import post_save

def create_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role=="student":

        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)

def send_invitation_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role=="student":
        send_mail(
        "Account creation confirmation",
        "Account created in codepilot",
        "anjalinbs@gmail.com",
        ["unt22cs016@uec.ac.in"],
        )

post_save.connect(send_invitation_mail,sender=User)
