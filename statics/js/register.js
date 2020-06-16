$(function(){
	$("#register").click(function(){

		var checkInput=0;	
		var userReg=/^[a-zA-Z\_][0-9a-zA-Z\_\$]{1,10}/;
		var pswReg=/[0-9a-zA-Z]{6,20}/;
		var user=$("#username").val();
		var psw=$("#password").val();
		var conPsw=$("#resurepassword").val();
			if(!userReg.test(user)||(user.length>10)){
				$('.user_error').text("The user name must be 1-10 characters consisting of numbers, letters, and underscores, and the first digit is letters or underscores");
				
			}else{
				checkInput+=1;
				$('.user_error').text("");
			}
			if(!pswReg.test(psw)||(psw.length<6 || psw.length>20)){
			  $('.psw_error').text("The password must be 6-20 digits or uppercase and lowercase alphabetic characters");
			}else{
				checkInput+=1;
				$('.psw_error').text("");
			}
			if(psw.length!==conPsw.length||psw!==conPsw){
				$('.conf_error').html("The password entered twice is different");
			}else{
				checkInput+=1;
				$('.conf_error').html("");
			}

			if(checkInput===3){
				console.log("!");
               $.ajax({  
                  type:"post",  
				  url:"/register/", //只能是站点下路径
                  data: {username:user,password:psw},//提交到php的数据  
                  dataType: "json",//回调函数接收数据的数据格式  
                   success: function(msg){  
						if(msg["iserror"]){$('.register_error').html(msg["error"]);}  
						else{window.location="/login/";}
					},  
                            
                   error: function(XMLHttpRequest, textStatus, errorThrown) {
						$('.register_error').text("Server Error");}

                });  
			  } else {
				  $('.register_error').text("");
			  }})

			})