$(function(){
	$("#login").click(function(){
			if($("#username").val()===""){
				$('.login-error').text('Username can not be empty');
			} else if ($("#password").val()===""){
			$('.login-error').text('Password can not be empty');
			}
			else{
				var sendData = {"username":$("#username").val(),"password":$("#password").val()}
				console.log(sendData);
				$.ajax({
					url:"/login/",
					type:"POST",
					data:sendData,
					datatype:'json',
					success:function(data){
						if(data["iserror"]) {$('.login-error').text(data["error"]);}
						else {window.location="/home/";}
					}
				})
		  }

			})
        })


