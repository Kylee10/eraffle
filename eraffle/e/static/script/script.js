var id = null;
var x = null;
pause = false;

function spin1(){
  var adder = 50;
  var counter = 0;
  var end = Math.floor(Math.random() * 300) + 100
  var elem = document.getElementsByClassName("container1");
  for (let index = 0; index < elem.length; index++) {
    elem[index].style.top = (-100 * index) + 'px'
  }
  var id = setInterval(ani, 1/1000)
  function ani(){
    for (let index = 0; index < elem.length; index++) {
      var x = elem[index].style.top
      var y = elem[index].innerText
      var pos = parseInt(x.replace('px',""))
      if(pos == 100){
        elem[index].style.top = (-100 * (elem.length-1)) + 'px'
      }else{
        pos+=adder
        elem[index].style.top = pos + 'px'
      }
      if(counter >= (end - (end * .25))){
        adder = 5
      }
      if(counter >= (end - (end * .10))){
        adder = 1
      }
      if(pos == 0 && counter >= end){
        console.log(y)
        document.getElementById('result1').value = elem[index].children[0].innerText + "_" + elem[index].children[1].innerText
        clearInterval(id)
      }
    }
    counter++
  }
}

function spin2(){
  var adder = 50;
  var counter = 0;
  var end = Math.floor(Math.random() * 300) + 100
  var elem = document.getElementsByClassName("container2");
  for (let index = 0; index < elem.length; index++) {
    elem[index].style.top = (-100 * index) + 'px'
  }
  var id = setInterval(ani, 1/1000)
  function ani(){
    for (let index = 0; index < elem.length; index++) {
      var x = elem[index].style.top
      var pos = parseInt(x.replace('px',""))
      if(pos == 100){
        elem[index].style.top = (-100 * (elem.length-1)) + 'px'
      }else{
        pos+=adder
        elem[index].style.top = pos + 'px'
      }
      if(counter >= (end - (end * .25))){
        adder = 5
      }
      if(counter >= (end - (end * .10))){
        adder = 1
      }
      if(pos == 0 && counter >= end){
        document.getElementById('result2').value = elem[index].children[0].innerText + "_" + elem[index].children[1].innerText
        clearInterval(id)
      }
    }
    counter++
  }
}

function spin3(){
  var adder = 50;
  var counter = 0;
  var end = Math.floor(Math.random() * 300) + 100
  var elem = document.getElementsByClassName("container3");
  for (let index = 0; index < elem.length; index++) {
    elem[index].style.top = (-100 * index) + 'px'
  }
  var id = setInterval(ani, 1/1000)
  function ani(){
    for (let index = 0; index < elem.length; index++) {
      var x = elem[index].style.top
      var pos = parseInt(x.replace('px',""))
      if(pos == 100){
        elem[index].style.top = (-100 * (elem.length-1)) + 'px'
      }else{
        pos+=adder
        elem[index].style.top = pos + 'px'
      }
      if(counter >= (end - (end * .25))){
        adder = 5
      }
      if(counter >= (end - (end * .10))){
        adder = 1
      }
      if(pos == 0 && counter >= end){
        document.getElementById('result3').value = elem[index].children[0].innerText + "_" + elem[index].children[1].innerText
        clearInterval(id)
      }
    }
    counter++
  }
}

function spin4(){
  var adder = 50;
  var counter = 0;
  var end = Math.floor(Math.random() * 300) + 100
  var elem = document.getElementsByClassName("container4");
  for (let index = 0; index < elem.length; index++) {
    elem[index].style.top = (-100 * index) + 'px'
  }
  var id = setInterval(ani, 1/1000)
  function ani(){
    for (let index = 0; index < elem.length; index++) {
      var x = elem[index].style.top
      var pos = parseInt(x.replace('px',""))
      if(pos == 100){
        elem[index].style.top = (-100 * (elem.length-1)) + 'px'
      }else{
        pos+=adder
        elem[index].style.top = pos + 'px'
      }
      if(counter >= (end - (end * .25))){
        adder = 5
      }
      if(counter >= (end - (end * .10))){
        adder = 1
      }
      if(pos == 0 && counter >= end){
        document.getElementById('result4').value = elem[index].children[0].innerText + "_" + elem[index].children[1].innerText
        clearInterval(id)
      }
    }
    counter++
  }
}

function spin5(){
  var adder = 50;
  var counter = 0;
  var end = Math.floor(Math.random() * 300) + 100
  var elem = document.getElementsByClassName("container5");
  for (let index = 0; index < elem.length; index++) {
    elem[index].style.top = (-100 * index) + 'px'
  }
  var id = setInterval(ani, 1/1000)
  function ani(){
    for (let index = 0; index < elem.length; index++) {
      var x = elem[index].style.top
      var pos = parseInt(x.replace('px',""))
      if(pos == 100){
        elem[index].style.top = (-100 * (elem.length-1)) + 'px'
      }else{
        pos+=adder
        elem[index].style.top = pos + 'px'
      }
      if(counter >= (end - (end * .25))){
        adder = 5
      }
      if(counter >= (end - (end * .10))){
        adder = 1
      }
      if(pos == 0 && counter >= end){
        document.getElementById('result5').value = elem[index].children[0].innerText + "_" + elem[index].children[1].innerText
        clearInterval(id)
      }
    }
    counter++
  }
}

function spin6(){
  var adder = 50;
  var counter = 0;
  var end = Math.floor(Math.random() * 300) + 100
  var elem = document.getElementsByClassName("container6");
  for (let index = 0; index < elem.length; index++) {
    elem[index].style.top = (-100 * index) + 'px'
  }
  var id = setInterval(ani, 1/1000)

  function ani(){
    for (let index = 0; index < elem.length; index++) {
      var x = elem[index].style.top
      var pos = parseInt(x.replace('px',""))
      if(pos == 100){
        elem[index].style.top = (-100 * (elem.length-1)) + 'px'
      }else{
        pos+=adder
        elem[index].style.top = pos + 'px'
      }
      if(counter >= (end - (end * .25))){
        adder = 5
      }
      if(counter >= (end - (end * .10))){
        adder = 1
      }
      if(pos == 0 && counter >= end){
        
        document.getElementById('result6').value = elem[index].children[0].innerText + "_" + elem[index].children[1].innerText
        clearInterval(id)
      }
    }
    counter++
  }
}

function spinAll(){
  var r1 = document.getElementById('result1').value
  var r2 = document.getElementById('result2').value
  var r3 = document.getElementById('result3').value
  var r4 = document.getElementById('result4').value
  var r5 = document.getElementById('result5').value
  var r6 = document.getElementById('result6').value
  if (r1 != "" && r2 != "" && r3 != "" && r4 != "" && r5 != "" && r6 != "") {
    openMyModal2()
  }else{
    spin1()
    spin2()
    spin3()
    spin4()
    spin5()
    spin6()
  }
}

function openMyModal(){
  var modal = document.getElementById("mySpinModal");
  modal.style.display = "block";
}
function myCloseModal() {
  var modal = document.getElementById("mySpinModal");
  modal.style.display = "none";
}

function openMyModal2(){
  var modal = document.getElementById("mySaveWinnersModal");
  modal.style.display = "block";
}
function myCloseModal2() {
  var modal = document.getElementById("mySaveWinnersModal");
  modal.style.display = "none";
}