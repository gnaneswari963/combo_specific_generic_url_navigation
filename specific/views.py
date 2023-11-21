from django.shortcuts import render

# Create your views here.
def employee(request):
    return render(request,'employee.html')

def manager(request):
    return render(request,'manager.html')