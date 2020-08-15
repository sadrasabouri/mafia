var i = 0;
function start() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 0;
    var time_from_start = 0;
    var id = setInterval(frame, 1000);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width += 100 / 45;
        time_from_start ++;
        elem.style.width = width + "%";
        elem.innerHTML = time_from_start;
        elem.style.backgroundColor = "rgb(" + time_from_start * 5 +", 138, 223)"; 
      }
    }
  }
}
