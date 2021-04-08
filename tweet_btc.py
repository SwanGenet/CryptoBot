from random import randint
import sys
from twython import Twython
from secret import *
import requests
import json
from datetime import *
from dateutil.relativedelta import relativedelta

def listToStringWithoutBrackets(list1):
    return str(list1).replace('[','').replace(']','')


def price_date():
    today = date.today()
    ten_years = today - relativedelta(years=10)
    five_years = today - relativedelta(years=5)
    two_years = today - relativedelta(years=2)
    one_year = today - relativedelta(years=1)

    tab_dates = [ten_years,five_years,two_years,one_year]


    result=requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false')
    result.status_code

    result.text

    dico_result = result.json()
    
    final = ""

    price = dico_result['bitcoin']['usd']
    
    
    final += "#Bitcoin Price : $" + str(price) + "\n"


    i=0
    while i < len(tab_dates) :
        result=requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start='+str(tab_dates[i])+'&end='+str(tab_dates[i]))
        result.status_code

        result.text

        dico_result = result.json()
        
        price = dico_result['bpi'][str(tab_dates[i])]

        final += "\nDate : " + str(tab_dates[i]) + " | Price : $" + str(listToStringWithoutBrackets(price))
        i+=1
    return final
        
tweetStr = price_date()
print (tweetStr)
   

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret) # Informations secrete relative au compte bot

api.update_status(status=tweetStr)


