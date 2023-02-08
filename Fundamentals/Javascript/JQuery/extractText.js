$(document).ready(function(){
    $("button").click(function extractText(){
        let textVal = $("#items li").map(function(){
            return this.textContent;
        }).get().join(", ");
        $("#result").text(textVal);
        
    })
}
)






/*function extractText() {
    let items = $("ul#items li")
        .toArray()
        .map(li => li.textContent)
        .join(", ");
    $("#result").text(items);
}*/