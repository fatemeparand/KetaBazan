from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    pass


#
# class UnicodeMobileValidator (RegexValidators):
#     pass