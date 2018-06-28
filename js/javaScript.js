window.onscroll = function() {myHeader();};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function myHeader() {
  if (window.pageYOffset >= sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}


//notification
function launch_notification() {
  var note = document.getElementById("notice");
  note.className = "show";
  setTimeout(function(){ note.className = note.className.replace("show", ""); }, 5000);
}