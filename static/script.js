// main js file for index.html



$(document).ready(function(){
    console.log('Page Loaded');

    // on click event of submit button
    $("#submit-data").click(function(){
        // post form data to /analyze
        $.ajax({
            type: 'POST',
            url: '/analyze',
            data: '{"artist":"' + $('#text').val() + '"}', // or JSON.stringify ({name: 'jonas'}),
            success: function(data) { alert('data: ' + data); },
            contentType: "application/json",
            dataType: 'json'
        });
    })

});

