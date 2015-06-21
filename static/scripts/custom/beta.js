$(document).ready(function(){

	var lesson_id = $('#lesson_id').val();

$('#new_course_form').submit(function(){
	message = {};
	message.title = $('#title').val();
	message.description = $('#description').val();

	$.post('new_beta_course/', JSON.stringify(message), function(response) {
		console.log(response);
		if(response == "success") {
			location.reload();
		}
	})
})


$('#new_lesson_form').submit(function() {
	message = {};
	message.title = $('#title').val();
	message.description = $('#description').val();
	message.course_id = $('.course_id').attr('id');
	console.log(message)
	$.post('../../../new_lesson/', JSON.stringify(message), function(response) {
		console.log(response);
		if(response == "success") {
			location.reload();
		}
	})
})

$('.close').on('click', function(){
	id = $(this).attr('id');
	$.post('../../../notification_close/'+ id + '/', function(response) {
		console.log('notification response ' + response);
	});
})

$('#edit_project_button').on('click', function(){
	if($('#project_id').length) {
		message = {};
		message.lesson_id = lesson_id;
		message.content = CKEDITOR.instances['edit_project'].getData();
		message.project_id = $('#project_id').val();

		console.log(message);

		$.post('../../../beta/edit_project/', JSON.stringify(message), function(response) {
			console.log(response);
			location.reload();
		})
	}
	else {
		message = {};
		message.lesson_id = lesson_id;
		message.content = CKEDITOR.instances['edit_project'].getData();

		console.log(message);

		$.post('../../../beta/edit_project/', JSON.stringify(message), function(response) {
			console.log(response);
			location.reload();
		})
	}
})










})