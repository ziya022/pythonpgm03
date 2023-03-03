from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Place
from .models import Q

#
# def about(request):
#     return render(request,'about.html')
#
# def contact(request):
#     return HttpResponse('VCX')


# def demo(request):
    # name ='INDIA'
    # return render(request,"index.html")
# Create your views here.
def demo(request):
    obj1=Place.objects.all()
    obj2=Q.objects.all()
    return render(request,"index.html",{'result':obj1 ,'output':obj2})





# def addition(request):
#     X=int(request.GET['num1'])
#     Y=int(request.GET['num2'])
#     rslt=X+Y
#     return render(request,"result.html",{'result':rslt})
# def Home(request):
#     return redirect('/')
# def about(request):
#    return render(request,'about.html')