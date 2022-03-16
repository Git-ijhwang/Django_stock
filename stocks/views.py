from django.shortcuts import render
import requests
import json
import yfinance as yf

# Create your views here.

def home(request):
    try:
        ticker = request.GET['ticker']

        print(ticker)

        # stock_api = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_164e36e7a3724832862845e735e6b726")
        stock_api = yf.Ticker(ticker)

        # stock_a = json.loads(stock_api.info)
        stock_a = stock_api.info
        change = stock_a.get("currentPrice") - stock_a.get("previousClose")
        print(stock_api.info.get("currentPrice"))
        # print(change)
        # print(stock_a.get("previousClose"))

        stock = stock_api.info


    except Exception as e:
        stock =""

    content = {'stock': stock, 'change':change}
    # test = {'change': change}

    return render(request, 'stocks/home.html', content  )
