from django.db import models

class EnergyCalculation(models.Model):
    vermogen = models.FloatField()
    uren_per_dag = models.FloatField()
    verbruik_per_dag = models.FloatField()
    kost_per_maand = models.FloatField()
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vermogen}W - {self.uren_per_dag}u/dag"