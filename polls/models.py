from django.db import models

class Object(models.Model):
    description_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.object_text
