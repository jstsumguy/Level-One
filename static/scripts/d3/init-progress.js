$(document).ready(function() {
    $.get('../get_progress/', function(response) {
        makePieChart(JSON.parse(response));
    })
})