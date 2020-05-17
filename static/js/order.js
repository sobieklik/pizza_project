$(document).ready(function(){
    $('#order_button').on('click', function(event) {

        event.preventDefault();
        var product = $('.post-form');
        var posting = $.post( product.attr('action'), product.serialize() );

        posting.done(function(data) {
            $("#cart").empty();
            $("#cart").append(data).hide().fadeIn(100);   

        });

        posting.fail(function(data) { 
            alert("Serwer nie odpowiada. Spróbuj ponownie");

        });
    });
});