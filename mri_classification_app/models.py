from django.db import models

class MRIImage(models.Model):
    image = models.ImageField(upload_to='mri_images')

    # Add any additional fields and methods as per your requirements
