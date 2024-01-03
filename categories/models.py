from django.db import models
import uuid
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, blank =True, null =True)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False,  

                            primary_key=True) 
    
    class Meta:
        verbose_name='category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name