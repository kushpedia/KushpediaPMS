from django.db import models
import uuid
from properties.models import Property
from categories.models import Category
# Create your models here.
class Rooms(models.Model):
    property = models.ForeignKey(Property,null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.CASCADE)
    description = models.CharField(max_length = 255, null = True, blank = True)
    featured_image = models.ImageField(null=True, blank=True)
    created =models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null = True, blank = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False,  

                            primary_key=True) 
    class Meta:
        verbose_name = 'rooms'
        verbose_name_plural ='rooms'
    
    def __str__(self):
        return self.property.name