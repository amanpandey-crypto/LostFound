from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    UID = models.CharField(max_length=20, default='')
    branch = models.CharField(max_length=20, default='')
    year = models.CharField(max_length=20, default='')
    contactno = models.CharField(max_length=20, default='')
    user_image=models.URLField(null=True)
    designation=models.CharField(max_length=30, default='')
    def __str__(self):
        return self.user.username


class ItemData(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    UID = models.CharField(max_length=15, default='')
    ItemID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=150, null=True)
    Location = models.CharField(default="", max_length=100)
    item_image = models.URLField(null=True)
    author=models.CharField(max_length=15, default='')
    Find_Date = models.DateTimeField(auto_now=True)
    company=models.CharField(max_length=30, default='Not available')
    color=models.CharField(max_length=10, null=True)
    amount=models.BigIntegerField(default=0)
    active = models.BooleanField(default=True)



class LostItem(models.Model):
    id = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    lost_image = models.URLField(null=True)
    title = models.CharField(max_length=2000)
    author = models.CharField(max_length=20,default='')
    description = models.CharField(max_length=2000,default='')
    lost_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

