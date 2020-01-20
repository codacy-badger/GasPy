from django.db import models

class Fornitore(models.Model):
    name = models.CharField(max_length=200)
    tipologia_prodotti = models.CharField(max_length=120)
