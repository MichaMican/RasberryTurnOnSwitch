var url = "127.0.0.1/write"
//3
function toggleComputer(status){
    var obj = '{"status":'+ status + '}';

    $.ajax(url, {
        data : obj,
        contentType : 'application/json',
        type : 'POST'})
}

window.onload = function() {
    //TODO: Read current state from JSON file and set switch according to that state
    document.getElementById("switch1").checked = false;
  };