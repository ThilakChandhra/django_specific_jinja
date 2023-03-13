from django.shortcuts import render

# Create your views here.
def specific2(request):
    d={'College':'NARAYANA ENGINEERING COLLEGE','City':'Nellore','State':'Andhra Pradesh'}
    return render(request,'second.html',context=d)