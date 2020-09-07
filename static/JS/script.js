var baseURL = "localhost:65136"

var urlToWrite = ```${baseURL}/write```;
var urlToRead = ```${baseURL}/status```;
function toggleComputer(status){

    var json={
        "status": status.checked
    };
    var jsonFile = JSON.stringify(json,0,4);
    $.ajax({
        url: urlToWrite,
        method: "POST",
        contentType: "application/json",
        processData: false,
        data: jsonFile
    });
}

window.onload = function() {
    $.getJSON(urlToRead, function(data){
        document.getElementById("switch1").checked = data.status;
        document.getElementById("switch1").visibility = "visible";
    });
  };