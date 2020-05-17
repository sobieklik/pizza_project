$(document).ready(function(){
    check_cart();

    $(document).on('click','.navbar-collapse.in',function(e) {
        //close coollapse navbar after click 
        if( $(e.target).is('a') ) {
            $(this).collapse('hide')
        }
    });

    $('.add_to_cart').submit(function(event) {
         // Stop form from submitting normally
        event.preventDefault();
        var product = $(this);
        // Send the data using post
        var posting = $.post( product.attr('action'), product.serialize() );
        posting.done(function(data) {
            check_cart(); 
        });   
        posting.fail(function(data) {
        alert("error");
                
        });
    })
   
    $('#cart_button').on('click',function(){
        var dataURL = $(this).attr('data-href');
        //open /cart using modal
        $('.modal-body').load(dataURL,function(){
            $('#myModal').modal({show:true});
        });
    }) 
        
    function check_cart(){
        //send data to server
        $.ajax({
          url: '/check_cart_len',
          dataType: 'json',
          success: function (data) {
            //if succes change number in indicator of cart length
            if (data.cart_len) {
              $(".badge").empty().append(data.cart_len);
            }
            else {
                $(".badge").empty();
            }
          }
        });
  
      };
    
      // load modal after payment with result of payment process
    if ($(".check_payment").length){;
        var dataURL = $(".check_payment").attr('data-href');
        $('.modal-body').load(dataURL,function(){
            $('#myModal').modal({show:true});
        });
    }

});
