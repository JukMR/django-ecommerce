from django.db import models


class Item(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    description_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, blank=True)
    email = models.EmailField(primary_key=True)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
