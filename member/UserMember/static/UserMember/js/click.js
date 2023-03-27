$(document).on('submit','.postBtn',function(e){
    e.preventDefault();

    $ajax({
        type: 'POST'
        url: '/sendMQTT'
        data: {
            led1:$('#led1').val(),
            status1:$('status1').val(),
        },
        success: function(data){

        }
    })
})