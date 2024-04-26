from django.db import models

# Create your models here.

class MessageImages(models.Model):
    image = models.ImageField(upload_to='whatsapp/images/')
    caption = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.image)
