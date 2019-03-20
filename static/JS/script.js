var urlToWrite = "http://127.0.0.1/write";
var urlToRead = "http://127.0.0.1/read";
//3
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
    //TODO: Read current state from JSON file and set switch according to that state
    $.getJSON(urlToRead, function(data){
        document.getElementById("switch1").checked = data.status;
    });
  };