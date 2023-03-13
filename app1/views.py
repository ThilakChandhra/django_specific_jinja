from django.shortcuts import render

# Create your views here.
def specific1(request):
    d={'Name':'Thilak Chandhra','Age':23,'Qualification':'MCA'}
    return render(request,'first.html',context=d)