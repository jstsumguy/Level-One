$(document).ready(function(){

	/* Register for event */
	$('.register').on('submit', function(){
		message = {};
		message['id'] = $(this).find('button').attr('id');

		$.post('../register_event/', JSON.stringify(message), function(response) {
			console.log(response);
			if(response == "success") {
				location.reload();
			}
		})
	})
})