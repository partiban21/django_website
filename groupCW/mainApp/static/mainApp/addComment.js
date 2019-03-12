console.log("Hello Partiban");
//when submit pressed on the form with id addComment run method, 
$(document).on('submit', '#addComment', function(e){
    e.preventDefault();
    console.log('In the method')
    $.ajax({
      type: 'POST',
      url: '/addComment/',//which python method to call
      dataType: 'html',
      headers:{
          'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val(),
      },
      data:{
        comment: $('#Article #comment').val(),//data to pass to python methods (views)
        article: $('#Article #article').val(),
      },
      success: function (response) {//on success go to this webpage
        console.log("Success.");
        window.location.href = 'http://127.0.0.1:8000/technology/';
      },
      error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        console.log("Something messed up");
      },
    });
});

$(document).on('submit', '#addComment2', function(e){
    e.preventDefault();
    console.log('In the method')
    $.ajax({
      type: 'POST',
      url: '/addComment/',
      dataType: 'html',
      headers:{
          'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val(),
      },
      data:{
        comment: $('#Article #comment2').val(),
        article: $('#Article #article2').val(),
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

$(document).on('submit', '#addComment3', function(e){
    e.preventDefault();
    console.log('In the method')
    $.ajax({
      type: 'POST',
      url: '/addComment/',
      dataType: 'html',
      headers:{
          'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val(),
      },
      data:{
        comment: $('#Article #comment3').val(),
        article: $('#Article #article3').val(),
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


