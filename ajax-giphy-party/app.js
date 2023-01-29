console.log("Let's get this party started!");
$("#giphyForm").on("submit", function(e){
    e.preventDefault();
    let searchInput = $("#searchInput").val()   
    searchGiphy(searchInput)

})

$("input[type=button]").on("click", function(e){
    $("#memeHolder").children().remove()
})

async function searchGiphy(searchTerm){
    const res = await axios.get(`http://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym`)
    $("#memeHolder").append(`<img src="${res.data.data[0].images.fixed_height.url}" />`)
    return res.data
}