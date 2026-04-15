from django.shortcuts import render
from .models import CalculationHistory

def index(request):
    history = CalculationHistory.objects.all().order_by('-created_at')
    return render(request, 'calculator/index.html', {'history': history})