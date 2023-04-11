var segundos = 0;
      var minutos = 0;
      var horas = 0;
      var cronometro = document.getElementById("cronometro");

      function start() {
        intervalo = setInterval(function() {
          segundos++;
          if (segundos == 60) {
            segundos = 0;
            minutos++;
          }
          if (minutos == 60) {
            minutos = 0;
            horas++;
          }
          cronometro.innerHTML =
            (horas ? (horas > 9 ? horas : "0" + horas) : "00") +
            ":" +
            (minutos ? (minutos > 9 ? minutos : "0" + minutos) : "00") +
            ":" +
            (segundos > 9 ? segundos : "0" + segundos);
        }, 1000);
      }

      function pause() {
        clearInterval(intervalo);
      }

      function reset() {
        clearInterval(intervalo);
        segundos = 0;
        minutos = 0;
        horas = 0;
        cronometro.innerHTML = "00:00:00";
      }

      window.onload = function() {
        cronometro.innerHTML = "00:00:00";
      };