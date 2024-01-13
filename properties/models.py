from django.db import models
import uuid
# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=255)  
    address = models.TextField(null=True, blank=True)  
    description = models.TextField(null=True, blank=True)
    num_of_floors = models.IntegerField(null=True, blank=True)
    num_rooms = models.PositiveIntegerField(null=True, blank=True) 
    year_built = models.PositiveIntegerField(null=True, blank=True)
    featured_image = models.ImageField(default="properties/default.png", null=True, blank=True)
    latitudes = models.FloatField(null=True, blank=True)
    longitudes = models.FloatField(null=True, blank=True)  
    is_available = models.BooleanField(default=True)  
    created =models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False,  

                            primary_key=True) 
    
    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'
    
    def __str__(self):
        return self.name

    @property
    def propertyImageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url