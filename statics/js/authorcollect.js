function save(data){
    $.ajax({
        url:"/authorsearch/",
        type:"POST",
        data: data,
        dataType: "json",
        success: function(msg){  
            if(msg["iserror"]) {
				alert(msg["message"]);
			}
			else {
				alert("Collect Success");
			}
			             
        },
                
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Server Error");
        }
    });
}