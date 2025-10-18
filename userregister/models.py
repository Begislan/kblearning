from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class DataUser(models.Model):
    username = models.TextField(null=True)
    email = models.EmailField(null=True)
    tel = PhoneNumberField(null=True)
    telInfo = models.TextField(default=0)
    password=models.TextField(null=True)
    def __str__(self):
        return self.username
    # phone = "+789543653453"
    # phone_Active = 0
    # if phone[0:4] == "+996":
    #     phone_Active = 1
    # phone=phone,phone_phone=p[phone_Active]
    # if phone_Active == 1:
    #     file = true
    # else:
    #     file = false
