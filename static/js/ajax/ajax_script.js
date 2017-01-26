var ajaxRequest; // The variable that makes Ajax possible!
function ajaxFunction() {
  try {

    // Opera 8.0+, Firefox, Safari
    ajaxRequest = new XMLHttpRequest();
    return ajaxRequest;
  } catch (e) {

    // Internet Explorer Browsers
    try {
      ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      return ajaxRequest;
    } catch (e) {

      try {
        ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
        return ajaxRequest;
      } catch (e) {

        // Something went wrong
        alert("Your browser broke!");
        return false;
      }
    }
  }
}
