var canvas = document.getElementById("canvas");
var c = canvas.getContext("2d");

function point(){
  c.beginPath();
  c.moveTo(500, 500);
}
function line(x, y){
  c.strokeStyle = 'rgb(' + parseInt(Math.random() * 255) + ',' + parseInt(Math.random() * 255) + ',' + parseInt(Math.random() * 255) + ')';
  c.lineTo(x, y);
  c.stroke();
  c.beginPath();
  c.moveTo(x,y);
}

function in_red(){
  c.beginPath();
  c.lineWidth = 10;
  c.strokeStyle = '#ff0000';
  c.moveTo(602, 500);
  c.lineTo(398, 500);
  c.stroke();
  c.moveTo(500, 602);
  c.lineTo(500, 398);
  c.stroke();
  c.moveTo(450, 450);
  c.lineTo(550, 450);
  c.stroke();
  c.moveTo(450, 450);
  c.lineTo(450, 550);
  c.stroke();
  c.moveTo(550, 550);
  c.lineTo(550, 450);
  c.stroke();
  c.moveTo(550, 550);
  c.lineTo(450, 550);
  c.stroke();
}

function caminata(){
  var cont_out = 0;
  for(ii = 0; ii < 5000; ii++){
    point();
    var a = 0;
    var b = 0;
    for(i = 0; i < 10; i+=1){
      var random_num = Math.floor(Math.random() * 4);
      // console.log(random_num);
      if(random_num == 0){
        a += 1;
      }
      if(random_num == 1){
        b += 1;

      }
      if(random_num == 2){
        a -= 1;

      }
      if(random_num == 3){
        b -= 1;
      }
      line(500 + (a * 50), 500 + (b*50));
    }
    if(a > 2 || b > 2 || a < -2 || b < -2 || (a > 1 && b > 1) || (a > 1 && b < -1) || (a < -1 && b > 1) || (a < -1 && b < -1)){
      cont_out ++;
    }
  }

  console.log(cont_out)
  var porcentaje = ((5000 - cont_out)/5000) * 100;
  console.log(porcentaje);
  document.getElementById("resultado").innerHTML = porcentaje;
  in_red();
}
