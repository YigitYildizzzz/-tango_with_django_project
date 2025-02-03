from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        
        counter = 1
        original_slug = self.slug
        while Category.objects.filter(slug=self.slug).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1

        super(Category, self).save(*args, **kwargs)
    def __str__(self):  
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128  
    URL_MAX_LENGTH = 200  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title