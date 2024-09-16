function _(el) {
    return document.getElementById(el);
  }
  
  function uploadFile() {
    var file = _("file").files[0];
    var formdata = new FormData();
    formdata.append("file", file);
    var ajax = new XMLHttpRequest();
    ajax.upload.addEventListener("progress", progressHandler, false);
    ajax.addEventListener("load", completeHandler, false);
    ajax.addEventListener("error", errorHandler, false);
    ajax.addEventListener("abort", abortHandler, false);
    ajax.open("POST", "{% url 'upload_data' %}"); // Update with your URL
    ajax.send(formdata);
  }
  
  function progressHandler(event) {
    _("loaded_n_total").innerHTML = "Uploaded " + event.loaded + " bytes of " + event.total;
    var percent = (event.loaded / event.total) * 100;
    _("progressBar").value = Math.round(percent);
    _("status").innerHTML = Math.round(percent) + "% uploaded... please wait";
  }
  
  function completeHandler(event) {
    var response = JSON.parse(event.target.responseText);
    if (response.status === 'success') {
      _("status").innerHTML = response.message;
    } else {
      _("status").innerHTML = response.message;
    }
    _("progressBar").value = 0; // Clear progress bar after upload
  }
  
  function errorHandler(event) {
    _("status").innerHTML = "Upload Failed";
  }
  
  function abortHandler(event) {
    _("status").innerHTML = "Upload Aborted";
  }
  