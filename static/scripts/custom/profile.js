$(document).ready(function(){
	var current = 0;
	var def;
	$('#profile').addClass('active');
	
	setTimeout(function(){
		$('.notification').fadeIn('slow');
	}, 1000);

	$('.close').on('click', function(){
		id = $(this).attr('id');
		$.post('../../notification_close/'+ id + '/', function(response) {
			console.log('notification response ' + response);
		});
	})



	$('.remove').on('click', function(event){
		c_id = $(this).attr('id');
		message = {};
		message.course = c_id;

		$.ajax({
			type: 'post',
			data: JSON.stringify(message),
			url: '../../unenroll/',
			success: function(response) {
				console.log('response ' + response);
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

	function clear_side_content(parent) {
		$lesson_container = parent.find('.lesson_side');
		$lesson_container.find('.lesson_title').text("");
		$lesson_container.find('.lesson_description').text("");
		parent.find('.students').find('.top_student_container').empty();
	}

	/* Sidebar content */
	$('span.more_icon').on('click', function(){
		console.log('clicked');
		course_id = $(this).attr('id');
		side_content = $(this).parent().parent().find('.side');
		if(current != parseInt(course_id)) {
			console.log('calling...');
			$.post('../../get_course_progress/'+course_id + '/', function(response){
				try 
				{
					data = JSON.parse(response);
					console.log(data)
					if(data['lesson'] != undefined && !jQuery.isEmptyObject(data['lesson'])) {
						current = course_id;
						clear_side_content(side_content);
						console.log('progress ' + data['progress']);
						//side_content.find('.lesson_side').find('.lesson_title').text(data['lesson']['name']);
						//side_content.find('.lesson_side').find('.lesson_description').text(data['lesson']['description']);

						// side_content.find('.students').find('.top_student_container').append('<ul class="student_list"></ul>')

						// for(var i=0; i < data['students'].length; i++) 
						// {
						// 	side_content.find('.students').find('.top_student_container').find('.student_list')
						// 	.append('<li>' + data['students'][i]['username'] + '</li>');
						// }
						init_dial(side_content.find('.lesson_side'), data['progress']);
						side_content.fadeIn();
					}
					else {
						console.log('else');
						init_dial(side_content.find('.lesson_side'), 0);
						side_content.fadeIn();
					}
				}// try
			catch(err) {
				console.log(err);
			}
			})// end post
		}
	})

	function init_dial(elm, val) {
		val = Math.round(val);
		console.log(val);
		$(elm).empty();
		$(elm).append('<input class="lesson_progress dial" data-readOnly="true" type="text" value="' + val + '" /> ');
		$(elm).find('.dial').knob({
  		'format' : function (value) {
     			return value + '%';
  			}
		});
	}

// end of document
});