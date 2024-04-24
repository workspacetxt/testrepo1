from django.shortcuts import render,redirect,HttpResponse
from .models import testmodel

# Create your views here.

def homepage(request):
    datais=testmodel.objects.all()
    context={
        'datais':datais,
    }
    return render(request,'home.html',context)


def formfunc(request):
    if request.method == 'POST':
        name_is= request.POST.get("field1")
        age_is= request.POST.get("field2")
        
        ab=testmodel(modelname=name_is,modelage=age_is)
        ab.save()
    return redirect(homepage)


