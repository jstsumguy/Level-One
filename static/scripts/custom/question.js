$(document).ready(function(){

var q_id = "{{ question.id }}";

/* Like Answer */
$('.like-answer').on('click', function(){
    console.log('clicked');
    message = {};
    message['answer_id'] = $(this).attr('id');
    $.post('../../../like_answer/', JSON.stringify(message), function(response) {
        console.log(response);
        if(response == "success") {
            location.reload();
        }
    })
})

/* Editor init */
$('#answer').on('click', function(){
    $(this).css('display', 'none');
    if($('#answer_question').length) {
        CKEDITOR.replace( 'answer_question', {
            language: 'en',
            uiColor: '#9AB8F3'
        });
        $('#answer_question').fadeIn();
        $('#submit_answer').fadeIn();
    }
})

$('#submit_answer').on('click', function(){
    $(this).prop("disabled",true);
    message = {};
    message.answer = CKEDITOR.instances['answer_question'].getData();
    message.question = q_id;
    console.log(message);
    // $.post('../../../new_answer/', JSON.stringify(message), function(response) {
    //     console.log(response);
    //     if(response == "success") {
    //         location.reload();
    //     }
    // })
})
})