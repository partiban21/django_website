console.log("Hello Partiban");

$(document).on('submit', '#addComment', function(e){
    e.preventDefault();
    console.log('In the method');
    article: $('#Article #article').val(),
    console.log(article);
    $.ajax({
      type: 'POST',
      url: '/addComment/',
      dataType: 'html',
      headers:{
          'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val(),
      },
      data:{
        comment: $('#Article #comment').val(),
        article: $('#Article #article').val(),
      },
      success: function (response) {
        console.log("Success.");
        window.location.href = 'http://127.0.0.1:8000/technology/';
      },
      error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        console.log("Something messed up");
      },
    });
});