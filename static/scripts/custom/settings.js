$(document).ready(function(){

	/* Init */
	// Get current status
	$.ajax({
		type: 'post',
		url: '../get_notifications/',
		success: function(response) {
			console.log(response);
			console.log(typeof(response))
			if(response.toLowerCase() == 'true')
			{
				console.log('true');
				$.fn.bootstrapSwitch.defaults.state = true;
				$.fn.bootstrapSwitch.defaults.size = 'large';
				$(".check").bootstrapSwitch();
			}
			else
			{
				console.log('false');
				$.fn.bootstrapSwitch.defaults.state = false;
				$.fn.bootstrapSwitch.defaults.size = 'large';
				$(".check").bootstrapSwitch();
			}
		}
	});

	$('#email_notifications').on('change', function() {
		console.log('email status ' + $(this).attr('checked'));
	})

	$('#profile_notifications').on('change', function() {
		console.log('profile status ' + $(this).attr('checked'));
	})

	$('.check').on('switchChange.bootstrapSwitch', function(event, state) {
  		updateNotificationState(state);
	});

	//$('.check').bootstrapSwitch('state', true);

	var updateNotificationState = function(state) {

		message = {};
		message.state = state;

		$.ajax({
			type: 'post',
			data: JSON.stringify(message),
			url: '../update_notifications/',
			success: function(response) {
				console.log(response);
			},
			async: true
		})

	}

	$('#general_button').on('click', function(){

		message = {};
		message.firstname = $('#firstname').val();
		message.lastname = $('#lastname').val();
		message.email = $('#email').val();

		$.ajax({
			type: 'post',
			data: JSON.stringify(message),
			url: '../change_settings/',
			success: function(response) {
				console.log(response);
				location.reload();
			}
		})
	})
})