from django.db import models

# Create your models here.
class works(models.Model):
    work_name=models.CharField(max_length=255)
    work_color=models.CharField(max_length=255)
    work_pic=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.work_name
class projects(models.Model):
    pro_pic=models.CharField(max_length=255)
    def __str__(self):
        return self.pro_pic
    
class contact_form_info(models.Model):
    name=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField()
    action_time=models.DateTimeField()
    is_error=models.BooleanField(default=False)
    is_success=models.BooleanField(default=False)
    error_message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name 