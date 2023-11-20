from django.shortcuts import render

# Create your views here.
def ifelse_condition(request):
    d={'a':10000,'b':5000}
    return render(request,'ifelse_condition.html',d)

def ifelif_condition(request):
    d={'a':1000,'b':5000,'c':20000}
    return render(request,'ifelif_condition.html',d)

def nexted_condition(request):
    d={'a':1000,'b':2000,'c':30000}
    return render(request,'nexted_condition.html',d)