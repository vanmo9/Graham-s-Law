from django.db import models
import datetime as dt 
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(default="defaultprofile.jpeg", upload_to = 'images/')
    bio = models.TextField(null=False)
    profile_name = models.CharField(max_length=60)

    def __str__(self):
        return self.profile_name  

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()  



#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)             
    

class Image(models.Model):    
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    image_comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_image = models.ImageField(default="default.jpeg", upload_to = 'images/')
    likes = models.IntegerField()

    def __str__(self):
        return self.image_name  

    def save_image(self):
        self.save()
    
    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update()

    class Meta:
        ordering = ['pub_date']    

    @classmethod
    def search_by_profile(cls,search_term):
        profiles = cls.objects.filter(profile__icontains=search_term)
        return profiles
    @classmethod
    def todays_images(cls,date):
        images = cls.objects.filter(pub_date__date = date)
        return images

class Follow(models.Model):
    followers = models.ForeignKey(User, on_delete=models.CASCADE,related_name = "followers")
    following = models.ForeignKey(User,on_delete=models.CASCADE, related_name = "following")

class Likes(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name="Likes" )
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE ,related_name='profilelikes')
    photo = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='photolikes') 


class Comment(models.Model):
    comment = models.CharField(max_length = 100, blank = True)
    image = models.ForeignKey(Image,on_delete=models.CASCADE , related_name = "comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name = "comments")

    def save_comment(self):
        self.save()

    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()
            



