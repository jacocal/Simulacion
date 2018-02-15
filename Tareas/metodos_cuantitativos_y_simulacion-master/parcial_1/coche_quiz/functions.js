function coche(dias){
  var rand_general = 0;
  var carros_por_dia = 0;
  var carr_type = 0;
  var costo = 0;
  var costo_total = 0;
  var costo_todo = 0;
  var arr = [];

  rand_general = Math.random() * 1;
  for(var i = 0; i < dias; i++){
    costo_total = 0;
    costo = 0;
    if(rand_general <= .05){
      carros_por_dia = 3;
    }else if(rand_general > .05 && rand_general <= .20){
      carros_por_dia = 4;
    }else if(rand_general > .20 && rand_general <= .50){
      carros_por_dia = 5;
    }else if(rand_general > .50 && rand_general <= .75){
      carros_por_dia = 6;
    }else if(rand_general > .75 && rand_general <= .90){
      carros_por_dia = 7;
    }else if(rand_general > .90 && rand_general <= 1){
      carros_por_dia = 8;
    }

    for(var j = 0; j < carros_por_dia; j++){
      costo = 0;
      carr_type = Math.floor(Math.random() * 3);
      rand_general = Math.random() * 1;
      if(carr_type == 0){
        if(rand_general <= .45){
          costo += 350;
        }else if(rand_general > .45  && rand_general <= .60){
          costo += 1575;
        }else if(rand_general > .60 && rand_general <= .80){
          costo += 1925;
        }else if(rand_general > .80 && rand_general <= .90){
          costo += 2540;
        }else if(rand_general > .90 && rand_general <= 1){
          costo += 700;
        }
      }
      else if(carr_type == 1){
        if(rand_general <= .25){
          costo += 550;
        }else if(rand_general > .25  && rand_general <= .50){
          costo += 1975;
        }else if(rand_general > .50 && rand_general <= .65){
          costo += 2545;
        }else if(rand_general > .65 && rand_general <= .85){
          costo += 2925;
        }else if(rand_general > .85 && rand_general <= 1){
          costo += 700;
        }
      }
      else if (carr_type == 2) {
        if(rand_general <= .10){
          costo += 750;
        }else if(rand_general > .10  && rand_general <= .25){
          costo += 2275;
        }else if(rand_general > .25 && rand_general <= .55){
          costo += 2845;
        }else if(rand_general > .55 && rand_general <= .95){
          costo += 3415;
        }else if(rand_general > .95 && rand_general <= 1){
          costo += 700;
        }
      }
      costo_total += costo;
    }
    costo_todo += costo_total;
    arr.push(costo_total);
  }

  promedio = costo_todo/dias;
  standar = math.std(arr);
  var a95 = promedio + ((standar/ Math.sqrt(dias)) * 1.96);
  var b95 = promedio - ((standar/ Math.sqrt(dias)) * -1.96);
  var a90 = promedio + ((standar/ Math.sqrt(dias)) * 1.65);
  var b90 = promedio - ((standar/ Math.sqrt(dias)) * -1.65);
  var a85 = promedio + ((standar/ Math.sqrt(dias)) * 1.42);
  var b85 = promedio - ((standar/ Math.sqrt(dias)) * -1.42);
  var a80 = promedio + ((standar/ Math.sqrt(dias)) * 1.28);
  var b80 = promedio - ((standar/ Math.sqrt(dias)) * -1.28);
  var a75 = promedio + ((standar/ Math.sqrt(dias)) * 1.15);
  var b75 = promedio - ((standar/ Math.sqrt(dias)) * -1.15);


  console.log("pr " + promedio);
  console.log("standar " + standar);

  document.getElementById("a75").innerHTML = a75;
  document.getElementById("a80").innerHTML = a80;
  document.getElementById("a85").innerHTML = a85;
  document.getElementById("a90").innerHTML = a90;
  document.getElementById("a95").innerHTML = a95;
  document.getElementById("b75").innerHTML = b75;
  document.getElementById("b80").innerHTML = b80;
  document.getElementById("b85").innerHTML = b85;
  document.getElementById("b90").innerHTML = b90;
  document.getElementById("b95").innerHTML = b95;
}

coche(5000);
