from django.db import models

class AddInstagram(models.Model):
    follower = models.CharField(max_length=255)
    follow = models.CharField(max_length=255)

    