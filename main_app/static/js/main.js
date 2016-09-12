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
            type:"GET",
            data:{treasure_id: element.attr("data_id")},
            success: function(response){
                        element.html(" " + response);
                      }
        });
    });
});