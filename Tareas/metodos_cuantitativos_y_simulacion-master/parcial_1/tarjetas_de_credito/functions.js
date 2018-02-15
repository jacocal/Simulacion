function pobre_vendedor(llamadas){
  var comision = 0;
  var rand_general = 0;
  var mujeres = 0;
  var hombres = 0;
  var mujer5 = 0;
  var mujer10 = 0;
  var mujer15 = 0;
  var hombre5 = 0;
  var hombre10 = 0;
  var hombre15 = 0;
  var hombre20 = 0;

  for(var i  = 0; i < llamadas; i++){
    rand_general = Math.random() * 1;
    // ¿Contesto?
    if(rand_general <= .30){
      rand_general = Math.random() * 1;
      // ¿Es mujer?
      if(rand_general <= .20){
        hombres ++;
        rand_general = Math.random() * 1;
        // Si es hombre, ¿Quiere la tarjeta?
        if (rand_general <= .25) {
          rand_general = Math.random() * 1;
          if(rand_general <= .1){ // Credito de 5000
            hombre5++;
            comision += 200;
          }else if (rand_general > .1 && rand_general <= .5) { // Credito de 10000
            hombre10++;
            comision += 400;
          }else if (rand_general > .5 && rand_general <= .8) { // Credito de 15000
            hombre15++;
            comision += 600;
          }else if (rand_general > .8 && rand_general <= 1) { // Credito de 20000
            hombre20++;
            comision += 800;
          }
        }
      }else{
        mujeres++;
        rand_general = Math.random() * 1;
        // No es hombre, ¿Quiere la tarjeta?
        if (rand_general <= .15) {
          rand_general = Math.random() * 1;
          if(rand_general <= .6){ // Credito de 5000
            mujer5++;
            comision += 200;
          }else if (rand_general > .6 && rand_general <= .9) { // Credito de 10000
            mujer10++;
            comision += 400;
          }else if (rand_general > .9 && rand_general <= 1) { // Credito de 15000
            mujer15++;
            comision += 600;
          }
        }
      }
    }
  }
  document.getElementById("comision").innerHTML = comision;
  document.getElementById("hombres").innerHTML = hombres;
  document.getElementById("mujeres").innerHTML = mujeres;
  document.getElementById("mujer10").innerHTML = mujer10;
  document.getElementById("mujer15").innerHTML = mujer15;
  document.getElementById("mujer5").innerHTML = mujer5;
  document.getElementById("hombre5").innerHTML = hombre5;
  document.getElementById("hombre10").innerHTML = hombre10;
  document.getElementById("hombre15").innerHTML = hombre15;
  document.getElementById("hombre20").innerHTML = hombre20;



}

pobre_vendedor(5000);
