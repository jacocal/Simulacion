function mismo_numero(numero, iteraciones, dias){
  var random_num = 0;
  var ganaste = 0;
  var probabilidad_ganaste = 0;
  for(ii = 0; ii < dias ; ii++){
    for( i = 0; i < iteraciones ; i++){
      random_num = Math.floor(Math.random() * iteraciones);
      if(random_num == numero){
        ganaste =+ 1;
      }
    }
  }
  probabilidad_ganaste = (ganaste/iteraciones) * 100;
  document.getElementById("mismo").innerHTML = probabilidad_ganaste;
  document.getElementById("iteraciones").innerHTML = iteraciones;
}

function diferente_numero(iteraciones, dias){
  var random_num_1 = 0;
  var random_num_2 = 0;

  var ganaste = 0;
  var probabilidad_ganaste = 0;
  for(ii = 0; ii < dias ; ii++){
    for( i = 0; i < iteraciones ; i++){
      random_num_1 = Math.floor(Math.random() * iteraciones);
      random_num_2 = Math.floor(Math.random() * iteraciones);

      if(random_num_1 == random_num_2){
        ganaste =+ 1;
      }
    }
  }
  probabilidad_ganaste = (ganaste/iteraciones) * 100;
  document.getElementById("diferente").innerHTML = probabilidad_ganaste;
  document.getElementById("iteraciones2").innerHTML = iteraciones;
}
mismo_numero(375, 50000, 365);
diferente_numero(50000, 365);
