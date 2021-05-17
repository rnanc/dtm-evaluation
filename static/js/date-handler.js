let age_input = document.getElementById("idade");

function getDate(){
  var dtToday = new Date();
  var day = dtToday.getDate();
  var month = dtToday.getMonth() + 1;
  var year = dtToday.getFullYear();

  if(month < 10){
    month = '0' + month.toString();
  }
  if(day < 10){
    day = '0' + day.toString();
  }

  var dtMax = year + '-' + month + '-' + day;
  age_input.setAttribute("max", dtMax);
}

age_input.addEventListener("load", getDate());
