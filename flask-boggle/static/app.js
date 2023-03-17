// Finishes game after 60 seconds
$("document").ready(function(){
    setTimeout(disableGuessing, 60000)
})

$("#guessForm").on("submit", e => {
    e.preventDefault()
    val  = e.target[0].value
    e.target[0].value = ""
    axios.post('/guess', {
        guess: val
    }).then(res => res.data)
    .then(res=> {
        $("#guessResult").text(val)
        if(res.trim() == "ok"){
        total = $("#score").text()
        $("#score").text(Number(val.length) + Number(total))
        }
    })

})

//disables input button
function disableGuessing(){
    $("#submitGuess").prop("disabled", true)
    total = Number($("#score").text())
    //sneds result to flask to record score
    axios.post('/sendResult', {
        "result" :  total
    }).then(res => res.data)
    .then(res => console.log(res))
}