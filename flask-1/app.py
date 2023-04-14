from flask import Flask, session, redirect, render_template, request, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "SecRETKey"
debug = DebugToolbarExtension(app)
currencyDecoder = CurrencyCodes()
acceptableCurrencies = 'AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,BBD,BDT,BGN,BHD,BIF,BMD,BND,BOB,BRL,BSD,BTC,BTN,BWP,BYN,BZD,CAD,CDF,CHF,CLF,CLP,CNH,CNY,COP,CRC,CUC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,FJD,FKP,GBP,GEL,GGP,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IMP,INR,IQD,IRR,ISK,JEP,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LRD,LSL,LYD,MAD,MDL,MGA,MKD,MMK,MNT,MOP,MRU,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SHP,SLL,SOS,SRD,SSP,STD,STN,SVC,SYP,SZL,THB,TJS,TMT,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,USD,UYU,UZS,VES,VND,VUV,WST,XAF,XAG,XAU,XCD,XDR,XOF,XPD,XPF,XPT,YER,ZAR,ZMW,ZWL'
currencyList = acceptableCurrencies.split(",")

@app.route("/")
def home_page():
    
    resultHolder = session.get('result', '')
    if resultHolder:
        session['result'] = ''

    return render_template("home.html", result=resultHolder)

@app.route("/form-submit", methods=["POST"])
def form_submit():
    convertFrom = request.form["startingCurrency"].upper()
    convertTo = request.form["endCurrency"].upper()
    amount = request.form["amount"]
    
    errors = validateValues(convertFrom, convertTo, amount)

    for error in errors:
        flash(error)
    
    if not errors:
        amountSymbol = currencyDecoder.get_symbol(convertTo)    
        data = requests.get(f'https://api.exchangerate.host/convert?from={convertFrom}&to={convertTo}&amount={amount}')
        result = data.json().get('result', 'INVALID')
        session["result"] = f'The result is {amountSymbol}{result}'
    
    return redirect("/")

def validateValues(startCurrency, endCurrency, amount):
    errorList = []
    
    if startCurrency not in currencyList:
        errorList.append(f'Invalid currency: {startCurrency}')
    
    if endCurrency not in currencyList:
        errorList.append(f'Invalid currency: {endCurrency}')
    
    if (not amount.isdigit()) or (int(amount) < 0):
        errorList.append(f'Invalid value for: Amount input')
    
    return errorList

