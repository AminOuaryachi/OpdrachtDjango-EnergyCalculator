from django.shortcuts import render
from .models import EnergyCalculation

def calculate(request):
    result = None
    history = EnergyCalculation.objects.order_by('-datum')[:5]
    
    if request.method == 'POST':
        vermogen = float(request.POST['vermogen'])
        uren = float(request.POST['uren_per_dag'])
        prijs = float(request.POST['prijs_kwh'])
        
        verbruik_per_dag = (vermogen * uren) / 1000
        kost_per_maand = verbruik_per_dag * 30 * prijs
        
        EnergyCalculation.objects.create(
            vermogen=vermogen,
            uren_per_dag=uren,
            verbruik_per_dag=round(verbruik_per_dag, 3),
            kost_per_maand=round(kost_per_maand, 2)
        )
        
        result = {
            'verbruik': round(verbruik_per_dag, 3),
            'kost': round(kost_per_maand, 2)
        }
    
    return render(request, 'energy_app/calculate.html', {
        'result': result,
        'history': history
    })