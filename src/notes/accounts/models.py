from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
import datetime
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)
    headline = models.CharField(null=True,blank=True,max_length=100)
    bio = models.TextField(null=True,blank=True)
    img = models.ImageField(upload_to='profile_img',null=True,blank=True)
    join_date = models.DateTimeField(null=True,blank=True,default=datetime.datetime.now)
    skils = models.CharField(max_length=100,null=True,blank=True)
    number_phone = models.CharField(max_length=12)
    
    def save(self,*args,**kwargs):
        if not self.slug :
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)
    
    def __str__(self):
        return '%s ' %(self.user.username)


def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
    
post_save.connect(create_profile,sender=User)