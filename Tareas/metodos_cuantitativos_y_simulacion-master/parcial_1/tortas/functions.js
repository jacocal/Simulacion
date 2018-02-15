// Me dijiste que te ponga aquí que este proyecto lo tomarás como si fué entregado en clase para lo de los 2 puntos extra 
// graicas :)


function tortas(dias){
  var totales =  new Array(5);
  var ganancia_dia = 0;

  for(compra = 1; compra <= 6; compra++){
    ganancia_dia = 0;
    for(i = 0; i < dias; i++){
      var rand = Math.random() * 1;
      if(rand <= .05){ // Pedi 1 docena = 12 panes
        venta = 1;
      }else if (rand > .05 && rand <= .15) { // Pedi 2 docena = 24 panes
        venta = 2;
      }else if (rand > .15 && rand <= .35) { // Pedi 3 docenas = 36 panes
        venta = 3;
      }else if (rand > .35 && rand <= .75) { // Pedi 4 docena = 48 panes
        venta = 4;
      }else if (rand > .75 && rand <= .95) { // Pedi 5 docena = 60 panes
        venta = 5;
      }else if (rand > .95 && rand <= 1) { // Pedi 6 docena = 72 panes
        venta = 6;
      }


      if((compra - venta) < 0){
        ganancia_dia += compra * 4 * 12;
        ganancia_dia += (compra - venta) * 5 * 12;
      }else if ((compra - venta) == 0) {
        ganancia_dia += compra * 4 * 12;
      }else {
        ganancia_dia += venta * 4 * 12;
        ganancia_dia += (compra - venta) * 1.5 * 12;
      }
    }

    totales[compra] = ganancia_dia;
    console.log(ganancia_dia);
  }
  for(i = 1; i <= 6; i++){
    console.log("Si pides " + i + " docenas de panes ganas " + totales[i]);
    document.write("<br> Si pides " + i + " docenas de panes ganas " + totales[i]);

  }
}

tortas(5000);
