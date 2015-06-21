$(document).ready(function(){

	$('#signup').on('click', function() {		
		message = {};
		username = $('#username').val();
		password = $('#password').val();
		email = $('#email').val();

		message.username = username;
		message.email = email;
		message.password = password;

		$.ajax({
			type: 'post',
			data: JSON.stringify(message),
			url: '../signup_complete/',
			success: function(response) {
				console.log(response);
				if(JSON.parse(response) == "success")
				{
					document.location.href = '../../';
				}
				else
				{
					$('#username_error').text("Username already exists");
					$('#username_error').css('color', 'red');
					$('#username_error').fadeIn('slow');
				}
			}
		})

	})
});