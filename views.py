from django.forms import forms
from django.http import request
from django.views.generic import TemplateView
from .scrape import getPrices
from django.shortcuts import render
from .form import ProductView



def home_view(request, *args, **kwargs):
   print(args, kwargs)
   print(request.user)
   forms= ProductView()
   return render(request, "index.html", {
       'form' : forms
   })

#def product_view(request, *args, **kwargs):
   #  my_context ={
   #       getPrices()
   #  }
   #  return getPrices(request,"index.html", my_context)

def show_result(request):
    if request.method=='POST':
        forms= ProductView(request.POST)
        if forms.is_valid():
            results = getPrices()
            
            return render(request, 'result.html', {
                'results' : results
            })
    else:
        forms= ProductView()
        return render(request, 'index.html',{
            'form': forms
        })

    


