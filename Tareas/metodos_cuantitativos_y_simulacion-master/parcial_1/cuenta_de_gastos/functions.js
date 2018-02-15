function costo(months, ingreso){
  var dinero = 0;
  for (var i = 0; i < months; i++) {
    var subtotal = 0;
    rand = Math.random() * 1;
    var costo_transporte = 0;
    if(rand <= .1666666){
      costo_transporte = 1300;
    }else if(rand > .166666 && rand <= .333333){
      costo_transporte = 1800;
    }else if(rand > .333333 && rand <= .50){
      costo_transporte = 2300;
    }else if(rand > .50 && rand <= .6666666){
      costo_transporte = 2800;
    }else if(rand > .6666666 && rand <= .833333){
      costo_transporte = 3300;
    }else if(rand > .833333 && rand <= 1){
      costo_transporte = 3800;
    }
    subtotal += ingreso - costo_transporte;
    if(subtotal < 0){
      subtotal -= ingreso * .20;
    }else{
      subtotal -= subtotal * .4;
    }
    dinero += subtotal;
  }
  console.log("total de dinero sobrante " + dinero);
  var ahorro = dinero * .3 ;
  console.log("Se recomienda ahorrar un 30% de los ingresos para tener un ahorro de " + ahorro);
  var diversion = dinero - ahorro;
  console.log("nos quedan " + diversion + " para diversion");
}
costo(5000, 3000);
