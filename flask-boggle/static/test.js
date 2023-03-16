let timerHolder

$("#guessForm").on("submit", e => {
    e.preventDefault()
    val  = e.target[0].value
    e.target[0].value = ""
    axios.post('/guess', {
        guess: val
    }).then(res => res.data)
    .then(res=> {
        console.log(res)
        
        $("#guessResult").text(val)
        console.log(res["result"])
        console.log(res["result"] == "ok")
        if(res["result"] == "ok"){
        total = $("#score").text()
        $("#score").text(Number(val.length) + Number(total))
        }
    })
    if(timerHolder){
        console.log(timerHolder)
        clearTimeout(timerHolder)
    }
    timerHolder = setTimeout(disableGuessing, 60000)
    console.log(timerHolder)
})

function disableGuessing(){
    console.log("reac")
    $("#submitGuess").prop("disabled", true)
}