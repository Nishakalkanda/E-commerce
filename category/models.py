from django.db import models

class category(models.Model):
    category_name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to= 'photos/categories', blank=True)
    
    def __str__(self):
        return self.category_name