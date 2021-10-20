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

class Category(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural='Categories'

class SubCategory(models.Model):
  name = models.CharField(max_length=24)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.name  

  class Meta:
    verbose_name_plural='Sub Categories'

class Rating(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
  product = models.ForeignKey('Product', on_delete=models.CASCADE)
  value = models.IntegerField()
  opinion = models.CharField(max_length=200)

  def __str__(self):
    return f'{self.user} gives {self.value}'
class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
  enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=9,decimal_places=2)
  # ratings = models.ManyToManyField(Rating, blank=True)
  # TODO: maybe use cloudinary to store pictures
  # photo = models.CharField(max_length=100,default='images/Enterprise/default.png')
  # photo_thumb = models.CharField(max_length=100,default='images/Enterprise/default.png')

  def __str__(self):
    return self.name