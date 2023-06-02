from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    user_interestings = [
        ('Technology', 'technology'),
        ('Art', 'art'),
        ('Web', 'web'),
        ('Internet', 'internet'),
    ]

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    phone = models.CharField(
        unique=True,
        max_length=20,
        null=True
    )

    user_interesting = models.CharField(choices=user_interestings, max_length=200, null=True, default='Persional')