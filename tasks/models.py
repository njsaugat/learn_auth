from django.db import models
from users.models import CustomUser

class Task(models.Model):

    PRIORITY_HIGH="H"
    PRIORITY_MEDIUM="M"
    PRIORITY_LOW="L"
    
    PRIORITY_CHOICES=((PRIORITY_HIGH,"high_priority"),
                      (PRIORITY_MEDIUM,"medium_priority"),
                      (PRIORITY_LOW,"low_priority"),)
    title=models.CharField(max_length=255)
    description=models.TextField()
    
    priority_type=models.CharField(max_length=1,choices=PRIORITY_CHOICES)

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    