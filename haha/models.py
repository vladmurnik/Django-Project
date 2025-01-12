from django.db import models

class Cipher(models.Model):
    text_cipher = models.CharField(max_length=2000)