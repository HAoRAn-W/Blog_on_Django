from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:32]

