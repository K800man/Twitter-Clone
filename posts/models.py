from django.db import models
from cloudinary.models import CloudinaryField

class Post(models.Model):
    class Meta(object):
        db_table = 'post' 

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body= models.CharField(
        'body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'created Datetime', blank=True, auto_now_add=True,
    )
    like_count = models.PositiveIntegerField(
       'Like Count',default=0, null=True, blank=True
    )
    image= CloudinaryField('image', blank=True, db_index=True  )


