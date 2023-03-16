
$("#guessForm").on("submit", e => {
    e.preventDefault()
    val  = e.target[0].value
    e.target[0].value = ""
    axios.post('/guess', {
        guess: val
    }).then(res => res.data)
    .then(res=> {
        console.log(res)
        $("#guessResult").text(res["result"])
    })
})