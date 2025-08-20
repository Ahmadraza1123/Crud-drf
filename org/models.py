from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Branch(models.Model):
    company = models.ForeignKey(
        Company,
        related_name='branches',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.company})"


class Building(models.Model):
    branch = models.ForeignKey(
        Branch,
        related_name='buildings',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.branch})"


class Floor(models.Model):
    building = models.ForeignKey(
        Building,
        related_name='floors',
        on_delete=models.CASCADE
    )
    number = models.IntegerField()

    def __str__(self):
        return f"Floor {self.number} ({self.building})"


class Room(models.Model):
    floor = models.ForeignKey(
        Floor,
        related_name='rooms',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} (Floor {self.floor.number})"

