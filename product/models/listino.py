from django.db import models

class Listino(models.Model):
    fornitore = models.ForeignKey("Fornitore", on_delete=models.CASCADE)
    date_start_sell = models.DateTimeField()
    date_end_sell= models.DateTimeField()
