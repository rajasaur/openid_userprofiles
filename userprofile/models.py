from django.contrib.auth.models import User
from django.db import models

from django.core.exceptions import ValidationError
from django.core import validators

class UserProfile(models.Model):
    user = models.ForeignKey(User)

    favourite_pet = models.CharField(max_length = 10)
    favourite_number = models.CharField(max_length = 10,
                                        validators = [validators.RegexValidator('\d+'), validators.MinLengthValidator(4)])

