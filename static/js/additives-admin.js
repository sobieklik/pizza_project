$(document).ready(function(){
	$(function(){
    
            

        $(".add-row > a").click(function(){
            
            if ( document.getElementById("id_additives_product-3-size" ) != null ){

               document.getElementById("id_additives_product-3-size").value = 'SMALL'; 
            }
            else if ( document.getElementById("id_additives_product-2-size" ) != null ){
            
                document.getElementById("id_additives_product-2-size" ).value = 'BIG';
            }
            else if ( document.getElementById("id_additives_product-1-size" ) != null ){

                document.getElementById("id_additives_product-1-size").value = 'MEGA';
            };
          
            
        });
    });
});
