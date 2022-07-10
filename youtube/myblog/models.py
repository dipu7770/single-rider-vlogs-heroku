from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
CATEGORY_CHOICES = (
    ('travel','TRAVEL'),
    ('dalyblog','DALYBLOG'),
    ('comedy','COMEDY'),
    ('short','SHORT'),
)

LANGUAGE_CHOICES = (
    ('bengali','BENGALI'),
    ('english','ENGLISH'),
    ('hindi','HINDI'),
)

STATUS_CHOICES = (
    ('RA' , 'RECENTLY ADDED'),
    ('MW' , 'MOST WATCHED'),
    ('TR' , 'TOP RATED'),
)

class Youtube(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='youtubes')
    banner = models.ImageField(upload_to='youtubes_banner')
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES , max_length=10)
    status = models.CharField(choices=STATUS_CHOICES , max_length=2)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    youtube_trailer = models.URLField()

    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True, null=True)

    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
        super(Youtube , self).save( *args , **kwargs)


    def __str__(self):
        return self.title
    
LINK_CHOICES = (
    ('D','DOWNLOAD LINK'),
    ('W','WATCH LINK'),
)

class YoutubeLink(models.Model):
    youtube = models.ForeignKey(Youtube, related_name='youtube_watch_link',on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES,max_length=1)
    link = models.URLField()

    def __str__(self):
        return str(self.youtube) 
    