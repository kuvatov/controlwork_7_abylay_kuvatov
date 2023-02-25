textarea = document.querySelector('textarea');
  if(textarea){
    textarea.addEventListener('input', autoResize, false);
    textarea.addEventListener('click', autoResize, false);
  }

    function autoResize() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    }


function checkbox_show_delete_button(id) {
  var checkBox = document.getElementById(id);
  var btn = document.getElementById('checkbox_delete_button');

  if (checkBox.checked == true){
    btn.style.display = "inline-block";
  } else {
    btn.style.display = "none";
  }
}

function checkAll(o) {
  var boxes = document.getElementsByTagName("input");

  for (var x = 0; x < boxes.length; x++) {
    var obj = boxes[x];
    if (obj.type == "checkbox") {
      if (obj.name != "check")
        obj.checked = o.checked;
    }
  }
}
