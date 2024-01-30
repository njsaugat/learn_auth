from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models
from django.core.validators import EmailValidator
class CustomUser(AbstractUser):
    email = models.CharField(
        "email",
        max_length=150,
        unique=True,
        help_text=
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ,
        validators=[EmailValidator(message="Enter a valid email address")],
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]
    
    bio=models.CharField(max_length=255,blank=True)
    cover_photo=models.ImageField(upload_to='covers/',null=True,blank=True)

    groups=models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',
        related_query_name='customuser'
    )
    
    user_permissions=models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user',
        related_name='customuser_set',
        related_query_name='customuser'
    )