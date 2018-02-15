function amigo_impuntual(dias){
  var contador = 0;
  for( var i = 0; i < dias ; i++ ){
    var rnd_el = Math.floor(Math.random() * 60);
    var rnd_ella = Math.floor(Math.random() * 60);
    if( rnd_ella >= rnd_el){
      var dif = rnd_ella - rnd_el;
      if (dif <= 20){
        contador += 1;
      }
    }else{
      var dif = rnd_el - rnd_ella;
      if (dif <= 15){
        contador += 1;
      }
    }
  }
  var promedio = contador/dias;
  console.log(promedio);
  console.log(contador);

  document.getElementById("resultado").innerHTML = promedio;

}


amigo_impuntual(5000);
