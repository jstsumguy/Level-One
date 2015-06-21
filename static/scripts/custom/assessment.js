$(document).ready(function(){

	var quiz_id = $('.quiz_id').attr('id');
    var type = "mcq";

	$('#submit').on('click', function(){
		message = {};
		message.answers = [];
        message.tf_answers = [];
		$('input[type=radio]:checked').each(function(){
            if($(this).hasClass('mcq')) {
                message.answers.push($(this).attr('id'));
            }
			else if($(this).hasClass('tfq')) {
                obj = {};
                obj['id'] = $(this).attr('id');
                obj['answer'] = $(this).val();
                message.tf_answers.push(obj);
            }
		});
		console.log(message);
		$.post('../../../submit_assessment/'+quiz_id+'/', JSON.stringify(message), function(response) {
			console.log(response);
			if(response.indexOf("success") > -1) {
				location.reload();
			}
		})
	})

    $('#add_question').on('click', function(){
        message = {};
        message['questions'] = [];
        message['quiz'] = quiz_id;
 
        $('.question').each(function(){
            question = {};
            question['choices'] = [];
            question['answer'] = null;
            question['content'] = $(this).find('.multiple_choice_question').val()

            $(this).find('.choice-container').each(function(){
                choice = $(this).find('.form-group').find('.choice');
                question['choices'].push(choice.val());
                if(choice.hasClass('answer')) {
                    question['answer'] = choice.val();
                }
            })
            message['questions'].push(question);
        })
        console.log(message.questions);
        $.post('../../../add_question/', JSON.stringify(message), function(response){
        	console.log(response);
        	if(response.indexOf("success") > -1){
        		location.reload();
        	}
        })
    })

    /* True/false question */
    $('#add_tf_question').on('click', function(){
        message = {};
        message['question'] = $('#tf_question').val();
        message['answer'] = $('#tf_type').find(":selected").val();
        message['quiz'] = quiz_id;
        console.log(message);
        $.post('../../../add_tf_question/', JSON.stringify(message), function(response) {
            console.log(response);
            if(response == "success") {
                location.reload();
            }
        })
    })

    $('input[type=radio]').on('click', function(){
        console.log('change');
        $(this).parent().parent().find('.choice').addClass('answer');
    });

    $('#question_type').on('change', function(){
        console.log('changed');
        selected = $("option:selected");
        if(selected.val() == "tfq") {
            type = selected.val();
            $('#add_content_form').css('display', 'none');
            $('#tfq_form').fadeIn();
        }
        else {
            type = "mcq";
            $('#tfq_form').css('display', 'none');
            $('#add_content_form').fadeIn();
        }
    })



})