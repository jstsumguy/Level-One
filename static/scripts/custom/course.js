$(document).ready(function() {

	var lesson_id;
	var active = false;

	setTimeout(function(){
		$('.notification').fadeIn('slow');
	}, 1800)

	/* Close notification */
	$('.close').on('click', function(){
		id = $(this).attr('id');
		$.post('../../../notification_close/'+ id + '/', function(response) {
			console.log('notification response ' + response);
		});
	})

	/* Enroll in course */
	$('.enroll').on('click', function(){
		course_id = $(this).attr('id');
		if(course_id != undefined) {
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
			})//end ajax
		}
	})

	$('.add-content').click(function(){
		console.log('clicked')
		lesson_id = $(this).attr('id');
		console.log(lesson_id)
		$('#lesson_id').val(lesson_id);
	})

	$('.remove').on('click', function(){
		lesson_id = $(this).attr('id');
		message = {};
		message.lesson_id = lesson_id;

		$.ajax({
			type: 'post',
			data: JSON.stringify(message),
			url: '../../../delete_lesson/',
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

	$('#new_lesson_show').click(function(){
		$('#new_lesson_form').fadeIn();
	})

	$('#new_lesson_form').submit(function(){
		message = {};
		message.course_id = $('#course_id').val();
		message.title = $('#title').val();
		message.description = $('#description').val();

		$.post('../../../new_lesson/', JSON.stringify(message), function(response) {
			if(response.indexOf("success") > -1) {
				location.reload();
			}
		})
	})

	/* Editor */
	var init_editor = function() {
		if($('#edit-course').length && !active) {
			active = true;
	        CKEDITOR.replace( 'edit-course', {
	            language: 'en',
	            uiColor: '#9AB8F3'
	        });
	    }
	};

    $('#edit-course-btn').click(function(){
        if(!$(this).hasClass('clicked')) {
            $(this).removeClass('btn-info');
            $(this).addClass('clicked');
            $(this).addClass('btn-success');
            $(this).text("Save");
            init_editor();
            $('.course-description').fadeOut();
    		$('#edit-course').fadeIn();
        }
        else {
            console.log('save clicked');
            message = {};
            message['course_id'] = $('.class_id').attr('id');
            message['content'] = CKEDITOR.instances['edit-course'].getData();
            console.log(message);
            $.post('../../../edit_course/', JSON.stringify(message), function(response) {
                console.log(response);
                if(response == "success") {
                    location.reload();
                }
            })
        }
    })


























});