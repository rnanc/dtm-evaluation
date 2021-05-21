$(document).ready(function(){
  let button_open = document.querySelector("#iniciar_open");
  let button_finish_open = document.querySelector("#finalizar_open");
  let button_finish_shut = document.querySelector("#finalizar_shut");
  let enviar_form = document.querySelector("#enviar_form");
  let camera_div = document.querySelector("#camera_div");
  let video = document.querySelector('#webCamera')
  let report_open = document.querySelector('#report_open')
  let report_shut = document.querySelector('#report_shut')

  let localMediaStream = null;
  let namespace = '/exam';
  let socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

  function takeShot(){
    var canvas = document.createElement('canvas');
	  canvas.width = video.videoWidth;
	  canvas.height = video.videoHeight;
	  var ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
    let dataURL = canvas.toDataURL('image/jpeg');
    return dataURL
  }

  button_finish_open.onclick = function () {
    socket.emit('open_measurement', takeShot());
    console.log("Enviado!")
    button_finish_shut.removeAttribute('hidden');
    button_finish_open.setAttribute('hidden', 'hidden')
  };

  button_finish_shut.onclick = function () {
    socket.emit('shut_measurement', takeShot());
    button_finish_shut.setAttribute('hidden', 'hidden');
    enviar_form.removeAttribute('disabled');
  };

  button_open.onclick = function (){
    camera_div.removeAttribute('hidden');
	  button_open.setAttribute('hidden', 'hidden');
	  button_finish_open.removeAttribute('hidden');
    OpenCam();
  };
  function OpenCam(){
	//Captura elemento de vídeo
    var video = document.querySelector("#webCamera");
      video.setAttribute('autoplay', '');
      video.setAttribute('muted', '');
      video.setAttribute('playsinline', '');

    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({audio: false, video: {facingMode: 'user'}})
      .then( function(stream) {
        //Definir o elemento vídeo a carregar o capturado pela webcam
        video.srcObject = stream;
      })
      .catch(function(error) {
        alert("Oooopps... Falhou :'(");
      });
    }
  }

  socket.on('connect', function() {
    console.log('Connected!');
  });

  socket.on('result_open',function(data){
    let boca_aberta = document.querySelector("#boca_aberta");
    let open_px = document.querySelector("#open_measurement_px");
    console.log(data.measurement);
    open_px.value = data.measurement;
    boca_aberta.innerHTML = data.measurement;
    report_open.value = data.img
  });

  socket.on('result_shut',function(data){
    let boca_fechada = document.querySelector("#boca_fechada");
    let resultado = document.querySelector("#resultado");
    let shut_px = document.querySelector("#shut_measurement_px");
    let result_cm = document.querySelector("#result_measurement_cm");
    boca_fechada.innerHTML = data.measurement;
    shut_px.value = data.measurement;
    resultado.innerHTML = data.result;
    result_cm.value = data.result;
    report_shut.value = data.img
    console.log(data.measurement);
    console.log(data.result);
  });

});




