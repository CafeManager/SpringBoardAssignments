$("a[data-delete-tag]").on("click", function(e){
    e.preventDefault()
    id = $(this).attr('data-id')
    try{
        axios.post(`/feedback/${id}/delete`).then(res => {
        if(res.status == 200){
            $(this).parent().parent().remove()
        }
    })
    }catch(error){
        console.log(`${error}`)
    }
})

