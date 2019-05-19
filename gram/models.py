from django.db import models
import datetime as dt

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length  = 60)
    photo_name = models.ForeignKey(NAME)
    c_name = models.ForeignKey(Category)
    photo = models.ImageField(upload_to = 'photo/')


    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    
