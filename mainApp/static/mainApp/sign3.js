console.log("Hello Partiban");
//there are so many sign files because when changes are made they do appear when running the code, 
//so new files with different names must be created to test changes
$(function(){
	$('#logusername').blur(function(){
		$.ajax({
			type: 'POST',
			url: '/logCheckUser/',
			data : {
				'username' : $('#logusername').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: checkuseranswer,
			dataType: 'html'
		});
	});
});

/*$(document).on('submit', '#signinForm', function(e){
    e.preventDefault();
    console.log('In the method');
    $.ajax({
      type: 'POST',
      url: '/login/',
      dataType: 'html',
      headers:{
          'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val(),
      },
      data:{
        username: $('.main #logusername').val(),
        password: $('.main #password').val(),
      },
      success: checkuseranswer, 
      error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        console.log("Something fucked up");
      },
    });
});*/

function checkuseranswer(data, textStatus, jqHXR)
{  
    /*console.log(data)
    if(data == "<span class='available'>&nbsp;&#x2714; Valid </span>"){
        window.location.href = 'http://127.0.0.1:8000/'
    }
    else{*/
        $('#info').html(data);
    /*}*/
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
                console.log("Something fucked up");
            }
        });
        return false
    });
    
});*/