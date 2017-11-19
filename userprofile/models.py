from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class About_us(models.Model):
    username = models.OneToOneField(User , on_delete=models.CASCADE,primary_key=True,related_name="xyz",)
    slug = models.SlugField(null=True, blank=True , unique=True)
    Name = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    Institute = models.CharField(max_length=200)
    Departmental_post = models.CharField(max_length=200)
    Room_no = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    ResearchInterest = models.CharField(max_length=200)
    LinkedinURL = models.CharField(max_length=200)

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username.username

    def get_absolute_url(self):
        return reverse('detail',kwargs={'slug':self.slug })

    def save(self, *args, **kwargs):
        self.s = slugify(self.username)
        super(About_us, self).save(*args, **kwargs)

class Teaching(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Teach")
    slug = models.SlugField(null=True, blank=True , unique=True)
    Institute = models.CharField(max_length=200)
    Course = models.CharField(max_length=200)
    Duration = models.CharField(max_length=200)

class Education(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Education")
    slug = models.SlugField(null=True, blank=True , unique=True)
    Institute = models.CharField(max_length=200)
    Program = models.CharField(max_length=200)
    Branch = models.CharField(max_length=200)
    Duration = models.CharField(max_length=200)

class Experience(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Experience")
    slug = models.SlugField(null=True, blank=True , unique=True)
    Designation = models.CharField(max_length=200)
    Company = models.CharField(max_length=200)
    Duration = models.CharField(max_length=200)

class Publications(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Publications")
    slug = models.SlugField(null=True, blank=True , unique=True)
    Title = models.CharField(max_length=200)
    URL = models.CharField(max_length=200)
    Year = models.CharField(max_length=200)
    Citations = models.CharField(max_length=200)
    Abstract = models.CharField(max_length=200)

class Projecting(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Project")
    slug = models.SlugField(null=True, blank=True , unique=True)
    Topic = models.CharField(max_length=200)
    Details = models.CharField(max_length=200)
    Year = models.CharField(max_length=200)

class Awards(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Awards")
    slug = models.SlugField(null=True, blank=True , unique=True)
    Title = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)
    Issuer = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)