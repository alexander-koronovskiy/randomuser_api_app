// Table update information
$("#search_form_input").click(function(){
    var text = $("#text").val();
    $.ajax({
      url: "/suggestions",
      type: "get",
      data: {jsdata: text},
      success: function(response) {
        $("#place_for_suggestions").html(response);
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });
});

// User update information
$("#user_update").click(function(){
    $.ajax({
      url: "/user_update",
      type: "get",
      data: {jsdata: ''},
      success: function(response) {
        $("#reviews").html(response);
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });
});

// Json file download
function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

document.getElementById("dwn-btn").addEventListener("click", function(){
    var filename = "data.json";
    $.ajax({
      url: "/users_info",
      type: "get",
      data: {jsdata: ''},
      success: function(response) {download(filename, response);}
    });
}, false);
