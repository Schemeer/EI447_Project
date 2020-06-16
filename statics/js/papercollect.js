function save(data){
	data["authors"] = data["authors"].join(",");
	data["affiliations"] = data["affiliations"].join(",");
	$.ajax({
		url:"/papersearch/",
		type:"POST",
		data:data,
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