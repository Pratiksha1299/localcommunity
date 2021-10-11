from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.timezone import now
from django.urls import reverse
phone_regex = RegexValidator(
        regex=r'[+](0|91)?[-][7-9]\d{8}',
        message="Phone number must be entered in the format: '+91-9999999999'. Up to 10 digits allowed."
    )

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    provider = models.CharField(max_length=100)
    provider_contact=models.CharField(validators=[phone_regex],max_length=14,blank=True,default='+91-')
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True,default=now)
    price = models.IntegerField(help_text="Price")
    cover = models.ImageField(null=True, blank=True, upload_to="cover_image/")

    def __str__(self):
        return self.name + " by " + self.provider


class PostQuery(models.Model):
    sno= models.AutoField(primary_key=True)
    query_type=models.CharField(max_length=50)
    query_detail=models.TextField(max_length=400)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    def __str__(self):
        return self.query_type[0:12]+ "...." + "by " + self.user.username
