function tiempo_de_servicio3(i){

  if(arguments[i + 1] <= 0.05){
    //tiempo de servicio 20
    tiempo = 20;
  }else if (arguments[i + 1] > 0.05 && arguments[i + 1] <= 0.15) {
    //tiempo de servicio 25
    tiempo = 25;
  }else if (arguments[i + 1] > 0.15 && arguments[i + 1] <= 0.35) {
    //tiempo de servicio 30
    tiempo = 30;
  }else if (arguments[i + 1] > 0.35 && arguments[i + 1] <= 0.60) {
    //tiempo de servicio 35
    tiempo = 35;
  }else if (arguments[i + 1] > 0.60 && arguments[i + 1] <= 0.72) {
    //tiempo de servicio 40
    tiempo = 40;
  }else if (arguments[i + 1] > 0.72 && arguments[i + 1] <= 0.82) {
    //tiempo de servicio 45
    tiempo = 45;
  }else if (arguments[i + 1] > 0.82 && arguments[i + 1] <= 0.90) {
    //tiempo de servicio 50
    tiempo = 50;
  }else if (arguments[i + 1] > 0.90 && arguments[i + 1] <= 0.96) {
    //tiempo de servicio 55
    tiempo = 55;
  }else if (arguments[i + 1] > 0.96 && arguments[i + 1] <= 1 ) {
    //tiempo de servicio 60
    tiempo = 60;
  }
  return tiempo;
}

function cola(){
  var length = arguments.length;
  var equipo_de_personas = 3;

  var cola = 0;
  var comieron = false;
  var termina = [];
  var tiempo_de_servicio3arr = [];
  var tiempo_de_servicio4 = [];
  var tiempo_de_servicio5 = [];
  var tiempo_de_servicio6 = [];
  var inicia_servicio = [];
  var termina = [];
  var tiempo_entre_llegadas = [];
  var hora_de_llegada_camion = [];
  var ocio = [];

  for( i = 0; i < length ; i++){
    if(arguments[i] <= 0.02){
      tiempo_entre_llegadas.push(20);
    }else if (arguments[i] > 0.02 && arguments[i] <= 0.10) {
      tiempo_entre_llegadas.push(25);
    }else if (arguments[i] > 0.10 && arguments[i] <= 0.22) {
      tiempo_entre_llegadas.push(30);
    }else if (arguments[i] > 0.22 && arguments[i] <= 0.47) {
      tiempo_entre_llegadas.push(35);
    }else if (arguments[i] > 0.47 && arguments[i] <= 0.67) {
      tiempo_entre_llegadas.push(40);
    }else if (arguments[i] > 0.67 && arguments[i] <= 0.82) {
      tiempo_entre_llegadas.push(45);
    }else if (arguments[i] > 0.82 && arguments[i] <= 0.92) {
      tiempo_entre_llegadas.push(50);
    }else if (arguments[i] > 0.92 && arguments[i] <= 0.97) {
      tiempo_entre_llegadas.push(55);
    }else if (arguments[i] > 0.97 && arguments[i] <= 1){
      tiempo_entre_llegadas.push(60);
    }
    tiempo_de_servicio3arr.push( tiempo_de_servicio3(i, 0.83761,0.14387,0.51321,0.72472,0.05466,0.84609,0.29735,0.59076,0.76355,0.29549,0.61958,0.17267,0.10061,0.45645,0.86754,0.35340));
    // tiempo_de_servicio4 = tiempo_de_servicio4(i, TODOS LOS NUMEROS AQUI);
    // tiempo_de_servicio5 = tiempo_de_servicio5(i, TODOS LOS NUMEROS AQUI);
    // tiempo_de_servicio6 = tiempo_de_servicio6(i, TODOS LOS NUMEROS AQUI);

    if(hora_de_llegada_camion[i] >= 240 && !comieron){
      comieron = true;
      cola += 30;
    }
    // total minutos entre las 11 y las 730  = 510
    if(i == 0){
      hora_de_llegada_camion.push(tiempo_entre_llegadas[i]);
      cola = 0;
    }else{
      hora_de_llegada_camion.push(hora_de_llegada_camion[i - 1] + tiempo_entre_llegadas[i]);
      ocio[i] = hora_de_llegada_camion[i] - termina[i - 1];
      cola = termina[i - 1] - hora_de_llegada_camion[i];
      if(cola < 0){
        cola = 0;
      }
    }
    inicia_servicio.push(hora_de_llegada_camion[i] + cola);
    termina[i] = inicia_servicio[i] + tiempo_de_servicio3arr[i];
    if(hora_de_llegada_camion[i] >= 510){
      console.log("No se realizará servicio");
    }else{
      console.log( tiempo_entre_llegadas[i] + " | " + hora_de_llegada_camion[i] + " | " + inicia_servicio[i] + " | " + tiempo_de_servicio3arr[i] + " | " + cola);
    }
  }

}

cola(0.48355,0.98977,0.06533,0.45128,0.15486,0.19241,0.15997,0.67940,0.90872,0.58997,0.68691,0.73488,0.23423,0.86675,0.56856);
