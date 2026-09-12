from django.db import models

class Rank(models.Model):
    rank_title = models.CharField(max_length=25)

    def __str__(self):
        return self.rank_title
    

class Personnel(models.Model):
    name = models.CharField(max_length=25) 
    rank = models.ForeignKey(
        Rank, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        )

    def __str__(self):
        return f"{self.name}-{self.rank}"

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name
    
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

    def __str__(self):
        return self.name
    
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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name
    
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

    def __str__(self):
        return self.name