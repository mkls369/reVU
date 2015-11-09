$(document).ready(function() {

	$("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });


    $('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/reviews/like_category/', {wine_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
    });

    $('#likes2').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/reviews/give_rating/', {wine_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes2').hide();
    });
    });

});
