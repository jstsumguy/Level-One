$(document).ready(function(){

	/* Enroll in course */
	$('.enroll').on('click', function(){
		course_id = $(this).attr('id');
		$.ajax({
			type: 'post',
			url: '../../../enroll/' + course_id + '/',
			success: function(response) {
				if(response.indexOf("success") > -1)
				{
					console.log("success");
					location.reload();
				}
				else
				{
					console.log("An error occured");
				}
			}
		})
	})

	// $('.course-set').each(function(){
	// 	kin = [];
	// 	kin.push($(this).children());
	// 	console.log(kin);
	// 	_class = null;
	// 	if(kin.length == 3) {
	// 		_class = 'col-md-4';
	// 	}
	// 	else if(kin.length == 2) {
	// 		_class = 'col-md-6';
	// 	}
	// 	else if(kin.length == 1) {
	// 		_class = 'col-md-12';
	// 	}
	// 	for(var i = 0; i < kin.length; i++) 
	// 	{
	// 		kin[i].addClass(_class);
	// 	}
	// })

	/* Hide/Reveal Courses */
	$('#programming_selector').on('click', function(){
		clear_pane();
		$(this).parent().css('background-color', '#9afe2e');  
		$(this).css('background-color', '#9afe2e'); 
		$(this).css('color', 'white');
		$('.programming').fadeIn('slow');
	})
	$('#web_selector').on('click', function(){
		clear_pane();
		$(this).parent().css('background-color', '#9afe2e'); 
		$(this).css('background-color', '#9afe2e'); 
		$(this).css('color', 'white');
		$('.web').fadeIn('slow');
	})
	$('#ui_selector').on('click', function(){
		clear_pane();
		$(this).parent().css('background-color', '#9afe2e'); 
		$(this).css('background-color', '#9afe2e'); 
		$(this).css('color', 'white');
		$('.ui').fadeIn('slow');
	})

	function clear_pane() {
		$('#programming_selector').parent().css('background-color', 'white');
		$('#programming_selector').css('background-color', 'white'); 
		$('#programming_selector').css('color', 'black');

		$('#web_selector').parent().css('background-color', 'white');
		$('#web_selector').css('background-color', 'white'); 
		$('#web_selector').css('color', 'black');

		$('#ui_selector').parent().css('background-color', 'white');
		$('#ui_selector').css('background-color', 'white'); 
		$('#ui_selector').css('color', 'black');

		$('.programming').css('display', 'none');
		$('.web').css('display', 'none');
		$('.ui').css('display', 'none');
	}


})