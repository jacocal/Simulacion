var aleatorioLlegadas = [0, -1, 0.48355,0.98977,0.06533,0.45128,0.15486,0.19241,0.15997,0.67940,0.90872,0.58997,0.68691,0.73488,0.23423,0.86675,0.56856];
var aleatorioServicio = [0, 0.83761,0.14387,0.51321,0.72472,0.05466,0.84609,0.29735,0.59076,0.76355,0.29549,0.61958,0.17267,0.10061,0.45645,0.86754,0.35340];
const dia = 510;
const horaComida = 300;

function probabilidadTiempoLlegadas(probabilidad) {
  if(probabilidad >= 0 && probabilidad <= 0.02){
    return 20;
  }else if (probabilidad > 0.02 && probabilidad <= 0.10) {
    return 25;
  }else if (probabilidad > 0.10 && probabilidad <= 0.22) {
    return 30;
  }else if (probabilidad > 0.22 && probabilidad <= 0.47) {
    return 35;
  }else if (probabilidad > 0.47 && probabilidad <= 0.67) {
    return 40;
  }else if (probabilidad > 0.67 && probabilidad <= 0.82) {
    return 45;
  }else if (probabilidad > 0.82 && probabilidad <= 0.92) {
    return 50;
  }else if (probabilidad > 0.92 && probabilidad <= 0.97) {
    return 55;
  }else if (probabilidad > 0.97 && probabilidad <= 1) {
    return 60;
  }
  return 0;
}

function calcularEsperaCamiones(resultados) {
  let total = 0;
  for(let i = 0; i < resultados.length; i++) {
    total += resultados[i].tiempoEsperaCamion;
  }
  return total;
}

function probabilidadTiempoServicio3(probabilidad) {
  if(probabilidad <= 0.05) {
    //tiempo de servicio 20
    return 20;
  }else if (probabilidad > 0.05 && probabilidad <= 0.15) {
    //tiempo de servicio 25
    return 25;
  }else if (probabilidad > 0.15 && probabilidad <= 0.35) {
    //tiempo de servicio 30
    return 30;
  }else if (probabilidad > 0.35 && probabilidad <= 0.60) {
    //tiempo de servicio 35
    return 35;
  }else if (probabilidad > 0.60 && probabilidad <= 0.72) {
    //tiempo de servicio 40
    return 40;
  }else if (probabilidad > 0.72 && probabilidad <= 0.82) {
    //tiempo de servicio 45
    return 45;
  }else if (probabilidad > 0.82 && probabilidad <= 0.90) {
    //tiempo de servicio 50
    return 50;
  }else if (probabilidad > 0.90 && probabilidad <= 0.96) {
    //tiempo de servicio 55
    return 55;
  }else if (probabilidad > 0.96 && probabilidad <= 1 ) {
    //tiempo de servicio 60
    return 60;
  }
  return 0;
}

function probabilidadTiempoServicio4(probabilidad) {
  if(probabilidad <= 0.05) {
    //tiempo de servicio 20
    return 15;
  }else if (probabilidad > 0.05 && probabilidad <= 0.2) {
    //tiempo de servicio 25
    return 20;
  }else if (probabilidad > 0.2 && probabilidad <= 0.4) {
    //tiempo de servicio 30
    return 25;
  }else if (probabilidad > 0.4 && probabilidad <= 0.6) {
    //tiempo de servicio 35
    return 30;
  }else if (probabilidad > 0.6 && probabilidad <= 0.75) {
    //tiempo de servicio 40
    return 35;
  }else if (probabilidad > 0.75 && probabilidad <= 0.87) {
    //tiempo de servicio 45
    return 40;
  }else if (probabilidad > 0.87 && probabilidad <= 0.95) {
    //tiempo de servicio 50
    return 45;
  }else if (probabilidad > 0.95 && probabilidad <= 0.99) {
    //tiempo de servicio 55
    return 50;
  }else if (probabilidad > 0.99 && probabilidad <= 1 ) {
    //tiempo de servicio 60
    return 55;
  }
  return 0;
}

function probabilidadTiempoServicio5(probabilidad) {
  if(probabilidad <= 0.1) {
    //tiempo de servicio 20
    return 10;
  }else if (probabilidad > 0.1 && probabilidad <= 0.28) {
    //tiempo de servicio 25
    return 15;
  }else if (probabilidad > 0.28 && probabilidad <= 0.5) {
    //tiempo de servicio 30
    return 20;
  }else if (probabilidad > 0.5 && probabilidad <= 0.68) {
    //tiempo de servicio 35
    return 25;
  }else if (probabilidad > 0.68 && probabilidad <= 0.78) {
    //tiempo de servicio 40
    return 30;
  }else if (probabilidad > 0.78 && probabilidad <= 0.86) {
    //tiempo de servicio 45
    return 35;
  }else if (probabilidad > 0.86 && probabilidad <= 0.92) {
    //tiempo de servicio 50
    return 40;
  }else if (probabilidad > 0.92 && probabilidad <= 0.97) {
    //tiempo de servicio 55
    return 45;
  }else if (probabilidad > 0.97 && probabilidad <= 1 ) {
    //tiempo de servicio 60
    return 50;
  }
  return 0;
}

function probabilidadTiempoServicio6(probabilidad) {
  if(probabilidad <= 0.12) {
    //tiempo de servicio 20
    return 5;
  }else if (probabilidad > 0.12 && probabilidad <= 0.27) {
    //tiempo de servicio 25
    return 10;
  }else if (probabilidad > 0.27 && probabilidad <= 0.53) {
    //tiempo de servicio 30
    return 15;
  }else if (probabilidad > 0.53 && probabilidad <= 0.68) {
    //tiempo de servicio 35
    return 20;
  }else if (probabilidad > 0.68 && probabilidad <= 0.8) {
    //tiempo de servicio 40
    return 25;
  }else if (probabilidad > 0.8 && probabilidad <= 0.88) {
    //tiempo de servicio 45
    return 30;
  }else if (probabilidad > 0.88 && probabilidad <= 0.94) {
    //tiempo de servicio 50
    return 35;
  }else if (probabilidad > 0.94 && probabilidad <= 0.98) {
    //tiempo de servicio 55
    return 40;
  }else if (probabilidad > 0.98 && probabilidad <= 1 ) {
    //tiempo de servicio 60
    return 45;
  }
  return 0;
}

function main3() {
  var comida = false;
  var resultados = [];
  let minutosTotales = 0;

  resultados.push({
    "tiempoEntreLlegada": 0,
    "tiempoLlegada": 0,
    "inicioServicio": 0,
    "tiempoServicio": 0,
    "terminaServicio": 0,
    "ocioPersonal": 0,
    "tiempoEsperaCamion": 0,
    "longitudCola": 0,
    "empleadosComieron": comida
  });

  for(var i = 1; i < aleatorioLlegadas.length; i++) {
    let tiempoEntreLlegada = 0, tiempoLlegada = 0, inicioServicio = 0, tiempoServicio = 0, terminaServicio = 0, ocioPersonal = 0, tiempoEsperaCamion = 0, longitudCola = 0;

    tiempoEntreLlegada = probabilidadTiempoLlegadas(aleatorioLlegadas[i]);
    tiempoLlegada = resultados[i - 1].tiempoLlegada + tiempoEntreLlegada;

    if(tiempoLlegada <= dia) {
      tiempoServicio = probabilidadTiempoServicio3(aleatorioServicio[i]);

      if (tiempoLlegada < resultados[i - 1].terminaServicio) {
        if(resultados[i - 1].terminaServicio >= horaComida && comida == false) {
          inicioServicio = resultados[i - 1].terminaServicio + 30;
          comida = true;
        } else {
          inicioServicio = resultados[i - 1].terminaServicio;
        }
      } else {
        if(tiempoLlegada >= horaComida && comida == false) {
          inicioServicio = tiempoLlegada + 30;
          comida = true;
        } else {
          inicioServicio = tiempoLlegada;
        }
      }

      terminaServicio = inicioServicio + tiempoServicio;
      minutosTotales = terminaServicio;

      if(tiempoLlegada > resultados[i - 1].terminaServicio) {
        ocioPersonal = tiempoLlegada - resultados[i - 1].terminaServicio;
      } else {
        ocioPersonal = 0;
      }

      if(tiempoLlegada < resultados[i - 1].terminaServicio) {
        tiempoEsperaCamion = resultados[i - 1].terminaServicio - tiempoLlegada;
      } else {
        tiempoEsperaCamion = 0;
      }

      if(tiempoLlegada < inicioServicio) {
        longitudCola = 1;
      } else {
        longitudCola = 0;
      }
    } else {
      longitudCola = resultados[i - 1].longitudCola + 1;
    }

    resultados.push({
      "tiempoEntreLlegada": tiempoEntreLlegada,
      "tiempoLlegada": tiempoLlegada,
      "inicioServicio": inicioServicio,
      "tiempoServicio": tiempoServicio,
      "terminaServicio": terminaServicio,
      "ocioPersonal": ocioPersonal,
      "tiempoEsperaCamion": tiempoEsperaCamion,
      "longitudCola": longitudCola,
      "empleadosComieron": comida
    });
  }

  let costoEmpleados = (dia/60) * 25;
  let costoAlmacen = (minutosTotales/60) * 500;
  let costoHorasExtra = (minutosTotales - dia)/60 * 37.50;
  let costoEsperaCamiones = (calcularEsperaCamiones(resultados)/60) * 100;
  let total = costoEmpleados + costoAlmacen + costoHorasExtra + costoEsperaCamiones;

  let final = {
    "tabla": resultados,
    "costoEmpleados": costoEmpleados,
    "costoAlmacen": costoAlmacen,
    "costoHorasExtra": costoHorasExtra,
    "costoEsperaCamiones": costoEsperaCamiones,
    "total": total
  };

  return final;
}

function main4() {
  var comida = false;
  var resultados = [];
  let minutosTotales = 0;

  resultados.push({
    "tiempoEntreLlegada": 0,
    "tiempoLlegada": 0,
    "inicioServicio": 0,
    "tiempoServicio": 0,
    "terminaServicio": 0,
    "ocioPersonal": 0,
    "tiempoEsperaCamion": 0,
    "longitudCola": 0,
    "empleadosComieron": comida
  });

  for(var i = 1; i < aleatorioLlegadas.length; i++) {
    let tiempoEntreLlegada = 0, tiempoLlegada = 0, inicioServicio = 0, tiempoServicio = 0, terminaServicio = 0, ocioPersonal = 0, tiempoEsperaCamion = 0, longitudCola = 0;

    tiempoEntreLlegada = probabilidadTiempoLlegadas(aleatorioLlegadas[i]);
    tiempoLlegada = resultados[i - 1].tiempoLlegada + tiempoEntreLlegada;

    if(tiempoLlegada <= dia) {
      tiempoServicio = probabilidadTiempoServicio4(aleatorioServicio[i]);

      if (tiempoLlegada < resultados[i - 1].terminaServicio) {
        if(resultados[i - 1].terminaServicio >= horaComida && comida == false) {
          inicioServicio = resultados[i - 1].terminaServicio + 30;
          comida = true;
        } else {
          inicioServicio = resultados[i - 1].terminaServicio;
        }
      } else {
        if(tiempoLlegada >= horaComida && comida == false) {
          inicioServicio = tiempoLlegada + 30;
          comida = true;
        } else {
          inicioServicio = tiempoLlegada;
        }
      }

      terminaServicio = inicioServicio + tiempoServicio;
      minutosTotales = terminaServicio;

      if(tiempoLlegada > resultados[i - 1].terminaServicio) {
        ocioPersonal = tiempoLlegada - resultados[i - 1].terminaServicio;
      } else {
        ocioPersonal = 0;
      }

      if(tiempoLlegada < resultados[i - 1].terminaServicio) {
        tiempoEsperaCamion = resultados[i - 1].terminaServicio - tiempoLlegada;
      } else {
        tiempoEsperaCamion = 0;
      }

      if(tiempoLlegada < inicioServicio) {
        longitudCola = 1;
      } else {
        longitudCola = 0;
      }
    } else {
      longitudCola = resultados[i - 1].longitudCola + 1;
    }

    resultados.push({
      "tiempoEntreLlegada": tiempoEntreLlegada,
      "tiempoLlegada": tiempoLlegada,
      "inicioServicio": inicioServicio,
      "tiempoServicio": tiempoServicio,
      "terminaServicio": terminaServicio,
      "ocioPersonal": ocioPersonal,
      "tiempoEsperaCamion": tiempoEsperaCamion,
      "longitudCola": longitudCola,
      "empleadosComieron": comida
    });
  }

  let costoEmpleados = (dia/60) * 25;
  let costoAlmacen = (minutosTotales/60) * 500;
  let costoHorasExtra = (minutosTotales - dia)/60 * 37.50;
  let costoEsperaCamiones = (calcularEsperaCamiones(resultados)/60) * 100;
  let total = costoEmpleados + costoAlmacen + costoHorasExtra + costoEsperaCamiones;

  let final = {
    "tabla": resultados,
    "costoEmpleados": costoEmpleados,
    "costoAlmacen": costoAlmacen,
    "costoHorasExtra": costoHorasExtra,
    "costoEsperaCamiones": costoEsperaCamiones,
    "total": total
  };

  return final;
}

function main5() {
  var comida = false;
  var resultados = [];
  let minutosTotales = 0;

  resultados.push({
    "tiempoEntreLlegada": 0,
    "tiempoLlegada": 0,
    "inicioServicio": 0,
    "tiempoServicio": 0,
    "terminaServicio": 0,
    "ocioPersonal": 0,
    "tiempoEsperaCamion": 0,
    "longitudCola": 0,
    "empleadosComieron": comida
  });

  for(var i = 1; i < aleatorioLlegadas.length; i++) {
    let tiempoEntreLlegada = 0, tiempoLlegada = 0, inicioServicio = 0, tiempoServicio = 0, terminaServicio = 0, ocioPersonal = 0, tiempoEsperaCamion = 0, longitudCola = 0;

    tiempoEntreLlegada = probabilidadTiempoLlegadas(aleatorioLlegadas[i]);
    tiempoLlegada = resultados[i - 1].tiempoLlegada + tiempoEntreLlegada;

    if(tiempoLlegada <= dia) {
      tiempoServicio = probabilidadTiempoServicio5(aleatorioServicio[i]);

      if (tiempoLlegada < resultados[i - 1].terminaServicio) {
        if(resultados[i - 1].terminaServicio >= horaComida && comida == false) {
          inicioServicio = resultados[i - 1].terminaServicio + 30;
          comida = true;
        } else {
          inicioServicio = resultados[i - 1].terminaServicio;
        }
      } else {
        if(tiempoLlegada >= horaComida && comida == false) {
          inicioServicio = tiempoLlegada + 30;
          comida = true;
        } else {
          inicioServicio = tiempoLlegada;
        }
      }

      terminaServicio = inicioServicio + tiempoServicio;
      minutosTotales = terminaServicio;

      if(tiempoLlegada > resultados[i - 1].terminaServicio) {
        ocioPersonal = tiempoLlegada - resultados[i - 1].terminaServicio;
      } else {
        ocioPersonal = 0;
      }

      if(tiempoLlegada < resultados[i - 1].terminaServicio) {
        tiempoEsperaCamion = resultados[i - 1].terminaServicio - tiempoLlegada;
      } else {
        tiempoEsperaCamion = 0;
      }

      if(tiempoLlegada < inicioServicio) {
        longitudCola = 1;
      } else {
        longitudCola = 0;
      }
    } else {
      longitudCola = resultados[i - 1].longitudCola + 1;
    }

    resultados.push({
      "tiempoEntreLlegada": tiempoEntreLlegada,
      "tiempoLlegada": tiempoLlegada,
      "inicioServicio": inicioServicio,
      "tiempoServicio": tiempoServicio,
      "terminaServicio": terminaServicio,
      "ocioPersonal": ocioPersonal,
      "tiempoEsperaCamion": tiempoEsperaCamion,
      "longitudCola": longitudCola,
      "empleadosComieron": comida
    });
  }

  let costoEmpleados = (dia/60) * 25;
  let costoAlmacen = (minutosTotales/60) * 500;
  let costoHorasExtra = (minutosTotales - dia)/60 * 37.50;
  let costoEsperaCamiones = (calcularEsperaCamiones(resultados)/60) * 100;
  let total = costoEmpleados + costoAlmacen + costoHorasExtra + costoEsperaCamiones;

  let final = {
    "tabla": resultados,
    "costoEmpleados": costoEmpleados,
    "costoAlmacen": costoAlmacen,
    "costoHorasExtra": costoHorasExtra,
    "costoEsperaCamiones": costoEsperaCamiones,
    "total": total
  };

  return final;
}

function main6() {
  var comida = false;
  var resultados = [];
  let minutosTotales = 0;

  resultados.push({
    "tiempoEntreLlegada": 0,
    "tiempoLlegada": 0,
    "inicioServicio": 0,
    "tiempoServicio": 0,
    "terminaServicio": 0,
    "ocioPersonal": 0,
    "tiempoEsperaCamion": 0,
    "longitudCola": 0,
    "empleadosComieron": comida
  });

  for(var i = 1; i < aleatorioLlegadas.length; i++) {
    let tiempoEntreLlegada = 0, tiempoLlegada = 0, inicioServicio = 0, tiempoServicio = 0, terminaServicio = 0, ocioPersonal = 0, tiempoEsperaCamion = 0, longitudCola = 0;

    tiempoEntreLlegada = probabilidadTiempoLlegadas(aleatorioLlegadas[i]);
    tiempoLlegada = resultados[i - 1].tiempoLlegada + tiempoEntreLlegada;

    if(tiempoLlegada <= dia) {
      tiempoServicio = probabilidadTiempoServicio6(aleatorioServicio[i]);

      if (tiempoLlegada < resultados[i - 1].terminaServicio) {
        if(resultados[i - 1].terminaServicio >= horaComida && comida == false) {
          inicioServicio = resultados[i - 1].terminaServicio + 30;
          comida = true;
        } else {
          inicioServicio = resultados[i - 1].terminaServicio;
        }
      } else {
        if(tiempoLlegada >= horaComida && comida == false) {
          inicioServicio = tiempoLlegada + 30;
          comida = true;
        } else {
          inicioServicio = tiempoLlegada;
        }
      }

      terminaServicio = inicioServicio + tiempoServicio;
      minutosTotales = terminaServicio;

      if(tiempoLlegada > resultados[i - 1].terminaServicio) {
        ocioPersonal = tiempoLlegada - resultados[i - 1].terminaServicio;
      } else {
        ocioPersonal = 0;
      }

      if(tiempoLlegada < resultados[i - 1].terminaServicio) {
        tiempoEsperaCamion = resultados[i - 1].terminaServicio - tiempoLlegada;
      } else {
        tiempoEsperaCamion = 0;
      }

      if(tiempoLlegada < inicioServicio) {
        longitudCola = 1;
      } else {
        longitudCola = 0;
      }
    } else {
      longitudCola = resultados[i - 1].longitudCola + 1;
    }

    resultados.push({
      "tiempoEntreLlegada": tiempoEntreLlegada,
      "tiempoLlegada": tiempoLlegada,
      "inicioServicio": inicioServicio,
      "tiempoServicio": tiempoServicio,
      "terminaServicio": terminaServicio,
      "ocioPersonal": ocioPersonal,
      "tiempoEsperaCamion": tiempoEsperaCamion,
      "longitudCola": longitudCola,
      "empleadosComieron": comida
    });
  }

  let costoEmpleados = (dia/60) * 25;
  let costoAlmacen = (minutosTotales/60) * 500;
  let costoHorasExtra = (minutosTotales - dia)/60 * 37.50;
  let costoEsperaCamiones = (calcularEsperaCamiones(resultados)/60) * 100;
  let total = costoEmpleados + costoAlmacen + costoHorasExtra + costoEsperaCamiones;

  let final = {
    "tabla": resultados,
    "costoEmpleados": costoEmpleados,
    "costoAlmacen": costoAlmacen,
    "costoHorasExtra": costoHorasExtra,
    "costoEsperaCamiones": costoEsperaCamiones,
    "total": total
  };

  return final;
}
