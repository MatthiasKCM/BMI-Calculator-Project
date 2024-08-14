from django.shortcuts import render, HttpResponse
from django.template import base


# Create your views here.
def calculate_bmi(weight, height):
    bmi = weight/height**2
    return round(bmi)

def index(request):
    if request.method == 'POST': #prüfen ob POST-request
        height = float(request.POST['height']) / 100 #speichern der Größe aus HTML-Template als Gleitzahl
        weight = float(request.POST['weight']) #speichern des Gewichts aus HTML-Template als Gleitzahl
        result = calculate_bmi(weight,height)
        return render(request, 'result.html',{'bmi': result})
    return render(request, 'base.html')