from django.db import models


class Feet(models.Model):
    name = models.CharField(max_length=60)
    width = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    radius = models.IntegerField(null=True, blank=True)


class Leg(models.Model):
    name = models.CharField(max_length=60)
    feet = models.ForeignKey(Feet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=60, unique=True)
    leg = models.OneToOneField(Leg, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('name', 'leg')

    def __str__(self):
        return self.name
