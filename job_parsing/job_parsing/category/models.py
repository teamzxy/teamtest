from django.db import models

class parsing(models.Model):
    post_name = models.CharField(max_length=100)
    post_path = models.CharField(max_length=200)
    post_category = models.CharField(max_length=100)

