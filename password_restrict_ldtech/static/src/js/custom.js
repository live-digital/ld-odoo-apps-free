$(document).ready(function(){
//jquery
   $(".oe_signup_form #password").focusout(function(ev){
		var password = $(".oe_signup_form #password").val()
		if(password){
			is_error = false
			if(password.length<8){
				is_error = true
			}else if($.isNumeric(password)){
				is_error = true
			}else if(/^[a-zA-Z]+$/.test(password)){
				is_error = true
			}
			if(is_error){
				$(".oe_signup_form #password").val('')
				$(".oe_signup_form #password").focus()
				//alert("Password must be 8 characters or more.\nMust contain the following:\n* atleast 1 Numeric number\n* atleast 1 Letter")
			}
  		}
	});
});