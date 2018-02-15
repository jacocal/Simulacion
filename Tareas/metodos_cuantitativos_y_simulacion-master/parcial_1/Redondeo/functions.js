function redondeo(){
  var rand = 0;
  var n99s = 0;
  var prov99 = 0;
  var prov100 = 0;
  var pago_cliente = 0;

  for(i = 0; i < 5000; i++){
    rand = Math.random() * 1;
    // console.log(rand);
    if(rand >= .20){
      n99s ++;
    }
    console.log(n99s);
  }

  prov99 = (n99s/5000) * 100;
  prov100 = ((5000 - n99s)/5000) * 100;
  pago_cliente = ((n99s * 99) + ((5000 - n99s) * 100))/5000;

  document.getElementById("99").innerHTML = prov99;
  document.getElementById("100").innerHTML = prov100;
  document.getElementById("cleinte").innerHTML = pago_cliente;

}

redondeo();
