from django.shortcuts import render

def home(request):
    import requests
    import json

    #Price
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=INR")
    price = json.loads(price_request.content)


    #News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request,'home.html',{'api':api,'price':price})

def prices(request):
    if request.method == 'POST':
        import requests
        import json

        #quote
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=INR")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote,'crypto': crypto})
    
    else:
        return render(request,'prices.html',{})