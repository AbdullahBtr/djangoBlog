from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.conf import settings

# Create your models here.

class Post(models.Model):
    body_text=models.TextField()
    title=models.CharField(max_length=50)
    created_on=models.DateField(auto_now_add=True)
    slug=models.SlugField(max_length=50,unique=True)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Post, self).save(*args, **kwargs)            


#Comment table 

class Comment(models.Model):
    text=models.TextField()
    email=models.EmailField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True)
    created_on=models.DateField(auto_now_add=True)
    post=models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment',
    )
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        related_name='author',
    )
    
    def __str__(self):
        return self.text


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author, allow_unicode=True)
        return super(Comment, self).save(*args, **kwargs)            
