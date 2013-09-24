from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(Owner)

    def __unicode__(self):
        return self.name
