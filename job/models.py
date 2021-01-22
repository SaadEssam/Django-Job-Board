from django.db import models
from django.utils.text import slugify

# Create your models here.

'''
Django Model Filed:
    - HTML Widget
    - Validation
    - DB Size
'''

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance, filename):
    imagename , extention = filename.split(".")
    return "job/%s.%s"%(instance.id, extention)


class Job(models.Model): # table
    title = models.CharField(max_length=100)  # column
    # Location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    Image = models.ImageField( upload_to=image_upload, height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(blank=True, null=True)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    