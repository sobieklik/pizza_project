$(document).ready(function(){
	$(function(){

        $('#id_category').change(function(){

            if (document.getElementsByClassName("inline-deletelink")[1] != null){      
                document.getElementsByClassName("inline-deletelink")[1].click();
            };
            
            if (document.getElementsByClassName("inline-deletelink")[0] != null){      
                document.getElementsByClassName("inline-deletelink")[0].click();
            };
        })
        
        $(".add-row > a").click(function(){
            
            if ( document.getElementById("id_food_product-1-size") != null){

                document.getElementById("id_food_product-1-size").value = 'SMALL';
            };
                    

        });
    });
});