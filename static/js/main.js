var i = 0;
function start() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 0;
    var time_from_start = 0;
    var id = setInterval(frame, 10);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width += 1 / 45;
        time_from_start = 45 * width / 100;
        elem.style.width = width + "%";
        elem.innerHTML = time_from_start.toFixed(2);
        elem.style.backgroundColor = "rgb(" + time_from_start * 6 +", 50, 50)"; 
      }
    }
  }
}
