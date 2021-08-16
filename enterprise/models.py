from django.db import models
from user_core.models import CustomUser

# Create your models here.
class Enterprise(models.Model):
  name = models.CharField(max_length=50,unique=True)
  description = models.CharField(max_length=500,blank=True)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  followers = models.ManyToManyField(CustomUser,blank=True,related_name='entreprises_followed')
  likes = models.ManyToManyField(CustomUser,blank=True,related_name='entreprises_liked')

  #new info to show on Enterprise contact sections
  address = models.CharField(max_length=100,blank=True)
  email = models.CharField(max_length=254,blank=True)
  url = models.CharField(max_length=100,blank=True)
  facebook = models.CharField(max_length=100,blank=True)
  twitter = models.CharField(max_length=100,blank=True)
  instagram = models.CharField(max_length=100,blank=True)
  youtube = models.CharField(max_length=100,blank=True)

  # province = models.ForeignKey(Province,null=True,blank=True)
  # municipality = models.ForeignKey(Municipality,null=True,blank=True)
  # TODO: maybe use cloudinary to store pictures
  # photo = models.CharField(max_length=100,default='images/Enterprise/default.png')
  # photo_thumb = models.CharField(max_length=100,default='images/Enterprise/default.png')
  # categories = models.ManyToManyField(Category,blank=True)

  def __str__(self):
    return "%s's %s" %(self.owner.user.username, self.name)

  def followers_count(self):
    return self.followers.count()

  def likes_count(self):
    return self.likes.count()