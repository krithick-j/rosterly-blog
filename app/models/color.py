from django.db import models



class Color(models.Model):
    color_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.color_name