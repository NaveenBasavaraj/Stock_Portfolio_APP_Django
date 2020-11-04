from django.shortcuts import render,redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

def home(request):
    #pk_156afab09225422d9e2078f39c6bd271
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        print("https://sandbox.iexapis.com/stable/stock/" + ticker + "/quote?token=Tpk_bfebc80f2c6e45cfa14df65d6f8c36c5")
        api_request = requests.get("https://sandbox.iexapis.com/stable/stock/" + ticker + "/quote?token=Tpk_bfebc80f2c6e45cfa14df65d6f8c36c5")

        try:
            api = json.loads(api_request.content)
            if not api:
                print(False)
        except:
            print(ticker)
            api = "Error...."
        return render(request,'home.html',{'api':api})
    else:
        return render(request,'home.html',{'ticker':'Enter a ticker symbol above'})


def about(request):
    return render(request,'about.html',{})

def add_stock(request):

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,("Stock has been added!"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        return render(request,'add_stock.html',{'ticker':ticker})