$(document).ready(function(){

    /**Add a button click event listener for the treasure likes
    Listens for any click events on these buttons, preventing default and capturing that button in a variable
    The AJAX request will call the /like_treasure/ url submitting a get request and submitting the data to the view
    The data will store the data id attribute of the clicked button
    The success function will capture the returned value and update the element*/
    $('button').on("click", function(event){
        event.preventDefault();
        var element = $(this);
        $.ajax({
            url:'/like_treasure/',
            type:"POST",
            data:{treasure_id: element.attr("data_id")},
            success: function(response){
                        element.html(" " + response);
                      }
        });
    });

    function csrfSafeMethod(method){
        //These methods to not require csrf protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
    }

    // This sets the csrf token inside the request header for any unsafe posts or non cross domain requests
    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            if(!csrfSafeMethod(settings.type) && !this.crossDomain){
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    // using gets the Cookie session for the user and stores the csrf token
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
});