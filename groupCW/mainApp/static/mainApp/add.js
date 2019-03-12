console.log("Hello Partiban");

$(document).on('submit', '#addUserForm', function(e){
    e.preventDefault();
    console.log('In the method');
    $.ajax({
      type: 'POST',
      url: '/addUser/',
      dataType: 'html',
      headers:{
          'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val(),
      },
      data:{
        email: $('.main #email').val(),
        fName: $('.main #firstName').val(),
        lName: $('.main #lastName').val(),
        phoneNum: $('.main #phoneNumber').val(),
        password: $('.main #password').val(),
      },
      success: function (response) {
        console.log("Success.");
        window.location.href = 'http://127.0.0.1:8000/';
      },
      error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        console.log("Something messed up");
      },
    });
});

function checkuseranswer(data, textStatus, jqHXR)
{
	$('#info').html(data);
}

/*$(function () {
    console.log("Ready");
    
    $('#addUserForm').submit(function (){
        $.ajax({
            url: '/addUser/',
            type: 'POST',
            data: 'html',
            success: function (response) {
                console.log("User is added.");
            },
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                console.log("Something messed up");
            }
        });
        return false
    });
    
});*/