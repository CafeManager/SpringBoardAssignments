$("document").ready(function(){
    getCupcakes()
})

$("#cupcake-form").on("submit", function(e){
    console.log(e)
})

function getCupcakes(){
    axios.get("/api/cupcakes").then(res => res.data).then(res => {
        console.log(res)
        for(cupcake of res["cupcakes"]){
            console.log(cupcake)
            $("#cupcake-holder").append(`
            <div class="mt-3 mb-3">
                <div class="row"> 
                    <div class="col-2">
                        <img class="image-resize" src=${cupcake.image}"/>
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