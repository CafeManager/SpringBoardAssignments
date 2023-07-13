$("document").ready(function () {
    getCupcakes()
})

$("#cupcake-form").on("submit", function (e) {
    e.preventDefault()
    labelElements = $('.input-group-text')
    formElements = $('.form-control')
    data = {}
    for (let i = 0; i < formElements.length; i++) {
        if (formElements[i].value) {
            label = labelElements[i].getAttribute("name")
            data[`${label}`] = formElements[i].value
        }
    }
    console.log(data)
    // Criticism Note: window.location.reload was the only way I can figure out to get the flask flashed messages to load. Maybe
    //there's a more elegant way of fixing? This feels "hacky"
    axios.post('/api/cupcakes', data).then(res =>
        window.location.reload(true)).catch(function (error) {
            console.log(error)
            window.location.reload(true)
        })

})

function getCupcakes() {
    $("#cupcake-holder").children().remove()
    axios.get("/api/cupcakes").then(res => res.data).then(res => {
        for (cupcake of res["cupcakes"]) {
            $("#cupcake-holder").append(`
            <div class="mt-3 mb-3">
                <div class="row"> 
                    <div class="col-2">
                        <img class="image-resize" src=${cupcake.image}>
                    </div>
                    <div class="col-10">
                        <div class="ms-3"> 
                            <div class="inline-block align-middle">
                            <p> Flavor: ${cupcake.flavor}</p>
                            <p> Size: ${cupcake.size}</p>
                            <p> Rating: ${cupcake.rating}</p>
                            </div>
                        </div>
                    </div>         
                </div>
            </div>
        `)
        }
    })
}