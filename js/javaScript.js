window.onscroll = function() {myFunction()};

const header = document.getElementById("myHeader");
const sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

$(document).ready(function(){
  $('#login1').tooltip('show');
  $('#login1').tooltip('hide');
});