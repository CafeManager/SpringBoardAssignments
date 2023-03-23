console.log("hi")
acceptableCurrencies = `AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,BBD,BDT,BGN,BHD,BIF,BMD,BND,BOB,BRL,BSD,BTC,BTN,BWP,BYN,BZD,CAD,CDF,CHF,CLF,CLP,CNH,CNY,COP,CRC,CUC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,FJD,FKP,GBP,GEL,GGP,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IMP,INR,IQD,IRR,ISK,JEP,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LRD,LSL,LYD,MAD,MDL,MGA,MKD,MMK,MNT,MOP,MRU,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SHP,SLL,SOS,SRD,SSP,STD,STN,SVC,SYP,SZL,THB,TJS,TMT,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,USD,UYU,UZS,VES,VND,VUV,WST,XAF,XAG,XAU,XCD,XDR,XOF,XPD,XPF,XPT,YER,ZAR,ZMW,ZWL`
currencyList = acceptableCurrencies.split(",")

$("#form").on("submit", e=> {
    e.preventDefault()
    console.log("reacg")
    convertFrom = e.target[0].value
    convertTo = e.target[1].value
    amount = e.target[2].value
    let result 
    errors = validateValues(convertFrom, convertTo)
    
    if(errors.length > 0){
        addErrorMessages(errors)
    }

    
    conversion = axios.get(`https://api.exchangerate.host/convert?from=${convertFrom}&to=${convertTo}&amount=${amount}`)
    .then(res=> {
        let data = res.data.result
        $("#result").text(``) 
        if(data){
        currencyString = convertNumberToCurrencyString(data)
        $("#result").text(`This is the ${currencyString}`)
        }
    })
   
})

function convertNumberToCurrencyString(number){
    result = parseFloat(number).toFixed(2)
    currencyString = Number(result).toLocaleString("en", {style:"currency", currency:`${convertTo}`})
    return currencyString
}

function validateValues(convertFrom, convertTo){
    $(".error").children().remove()
    boolCheckValidFrom = currencyList.find( e => e==convertFrom.toUpperCase())
    boolCheckValidTo = currencyList.find( e => e==convertTo.toUpperCase())
    
    errorList = []
    if(!boolCheckValidFrom){
        errorList.push(`Invalid currency: ${convertFrom}`)
    }
    if(!boolCheckValidTo){
        errorList.push(`Invalid currency: ${convertTo}`)
    }
    return errorList
}

function addErrorMessages(errorList){
    console.log(errorList)
    errorList.forEach(element => {
        $(".error").append(`<p class="error-message-padding"> ${element} </p>`)
    });
}