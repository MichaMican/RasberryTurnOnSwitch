var baseURL = "192.168.178.47:61772"

var urlToWrite = `/write`;
var urlToRead = `/status`;
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
        document.getElementById("switchInput").checked = data.status;
        document.getElementById("switchLabel").style.visibility = "visible";
    });
  };
