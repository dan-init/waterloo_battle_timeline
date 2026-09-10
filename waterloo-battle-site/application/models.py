from django.db import models

class Personnel(models.Model):
    name = models.CharField(max_length=25) 
    rank = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name} {self.rank}"

class Army(models.Model):
    name = models.CharField(max_length=10)
    primary_uniform_colour = models.CharField(max_length=10)
    size = models.PositiveIntegerField()
    commander = models.ForeignKey(
        Personnel, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

class Corp(models.Model):
    affiliated_army = models.ForeignKey(
        Army, 
        on_delete=models.SET,
        null=True
        )
    name = models.CharField(max_length=25)
    size = models.PositiveIntegerField()
    commander = models.ForeignKey(
        Personnel, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

class Division(models.Model):
    affiliated_corp = models.ForeignKey(
        Corp, 
        on_delete=models.SET_NULL,
        null=True
        )
    name = models.CharField(max_length=25)
    size = models.PositiveIntegerField()
    commander = models.ForeignKey(
        Personnel, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

class Bridade(models.Model):
    affilated_division = models.ForeignKey(
        Division, 
        on_delete=models.SET_NULL,
        null=True
        )
    name = models.CharField(max_length=25)
    size = models.PositiveIntegerField()
    commander = models.ForeignKey(
        Personnel, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

class Regiment(models.Model):
    affilated_brigade = models.ForeignKey(
        Bridade, 
        on_delete=models.SET_NULL,
        null=True
        )
    name = models.CharField(max_length=25)
    size = models.PositiveIntegerField()
    commander = models.ForeignKey(
        Personnel, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

class Battalion(models.Model):
    affliated_regiment = models.ForeignKey(
        Regiment, 
        on_delete=models.SET_NULL,
        null=True
        )
    name = models.CharField(max_length=25)
    size = models.PositiveIntegerField()
    commander = models.ForeignKey(
        Personnel, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

class Company(models.Model):
    affliated_battalion = models.ForeignKey(
        Battalion, 
        on_delete=models.SET_NULL,
        null=True
        )
    name = models.CharField(max_length=25)
    size = models.PositiveIntegerField()
    commander = models.ForeignKey(
        Personnel, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
