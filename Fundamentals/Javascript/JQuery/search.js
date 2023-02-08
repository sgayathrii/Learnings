$(document).ready(function(){
    $("button").click(function search(){
        let searchVal = $("#searchText").val();
        let count = 0;
        $("li").each(function(index, item){
                if(item.textContent.includes(searchVal))
                  {
                    count++;
                  }               
         })        
         $("#result").text(count + " matches found.");
         })
    })
            
 



       


