$(document).ready(function(){

    $('.add').submit(function(event) {
    
        event.preventDefault();
        var product = $(this);
        var posting = $.post( product.attr('action'), product.serialize());
        
        posting.done(function(data) {
        
            $("#cart").empty().append(data);  
            check_cart(); 
        
        });
        
        posting.fail(function(data) { 
        alert("Błąd serwera");
        
        });
    });
    
    $('#order').on('click',function(){
        
        var order = $('#order');
        var token = $('input[name="csrfmiddlewaretoken"]').attr('value');
        var dict = {}; // create dictionary that will be nested dictionary

        // for each ".form_sauce", ".form_meat", ".form_chips" create dictionary with contain selected value from form 
        $(".form_sauce").each(function() 
        {
    
            if( dict[this.name] === undefined){
                dict[this.name]={}; 
                dict[this.name]["sauce"]={}; 
                dict[this.name]["meat"]=[]; 
                dict[this.name]["chips"]=[];    
            };
         
            let e = this.querySelector('select[name ="sauce"]'); // find 'select[name ="sauce"]' in this ".form_sauce"
            let selectedid = e.options[e.selectedIndex].text;
    
            if ( dict[this.name]["sauce"][selectedid] === undefined){
                dict[this.name]["sauce"][selectedid]=1;
            }
            else dict[this.name]["sauce"][selectedid]+=1;  // modify quantity of the same sauce of selected product
    
        });
    
        $(".form_meat").each(function() {
            if( dict[this.name] === undefined){
                dict[this.name]={}; 
                dict[this.name]["sauce"]={}; 
                dict[this.name]["meat"]=[]; 
                dict[this.name]["chips"]=[];      
            };
    
            let e = this.querySelector('select[name ="meat"]');
            let selectedid = e.options[e.selectedIndex].text;
            dict[this.name]["meat"].push(selectedid);
        });
    
        $(".form_chips").each(function() {
            if( dict[this.name] === undefined){
                dict[this.name]={}; 
                dict[this.name]["sauce"]={}; 
                dict[this.name]["meat"]=[]; 
                dict[this.name]["chips"]=[]; 
            };
    
            let e = this.querySelector('select[name ="chips"]');
            let selectedid = e.options[e.selectedIndex].text;
            dict[this.name]["chips"].push(selectedid); 
        });
    
        dict_json = JSON.stringify(dict); // make JSON dictionary
      
        $.ajax({
            url: order.attr('data-href'),
            type: 'POST',
            data:{
                dict : dict_json,
                csrfmiddlewaretoken: token,  
                },
            success: function (data) {    
            
                $("#cart").empty();
                $("#cart").append(data).hide().fadeIn(700);   //insert another html page in "#cart" which will be displayed in modal
            },
            error: function() {
                alert("Serwer nie odpowiada. Spróbuj ponownie");
            }       
        });
               
    }); 
    
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
});