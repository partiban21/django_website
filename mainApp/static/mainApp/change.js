console.log("Hello Partiban");
//on submit click of form with id changeUserForm
$(document).on('submit', '#changeUserForm', function(e){
    e.preventDefault();
    console.log('In the method');
    $.ajax({
      type: 'PUT',
      url: '/editProfile/',
      dataType: 'html',
      headers:{
          'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val(),
      },
      data:{
        fName: $('.main #firstName').val(),//data passed to python methods
        lName: $('.main #lastName').val(),
        phoneNum: $('.main #phoneNumber').val(),
        password: $('.main #password').val(),
      },
      success: function(){
        console.log("Success");
        window.alert("Edit Successful");
        //$('.products_list ul #'+product_id+ ' a').text(update_name);
      },
      error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        console.log("Something messed up");
      },
    });
});

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
