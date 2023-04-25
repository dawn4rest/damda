from django.db import models


class Dam(models.Model):
    canvas = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.user_name