let rows = document.querySelectorAll("tbody tr");

for (let row of rows) {
  row.addEventListener("click", function () {
    window.location.href = "/details/" + row.id;
  });
}

//Function to research patients in table.
let search_box = document.getElementById("search_box");
function getListPatients() {
  patients_names = [];
  patients_tr = [];
  for (let row of rows) {
    patients_names.push(row.firstElementChild.firstChild.data.toLowerCase());
    patients_tr.push(row);
  }
  patients_names_filter = [];
  patients_names.forEach((element) => {
    if (element.indexOf(this.value.toLowerCase()) == 0) {
      patients_names_filter.push(element);
    }
  });
  if (this.value == null) {
    for (let row of patients_tr) {
      row[i].style = "display: flex;";
    }
  } else {
    for (let i in patients_tr) {
      nome_aux = patients_names[i];
      if (patients_names_filter.indexOf(nome_aux) > -1) {
        rows[i].style = "display: flex;";
      } else {
        rows[i].style = "display: none;";
      }
    }
  }
}
search_box.addEventListener("input", getListPatients);
search_box.addEventListener("change", getListPatients);

function changePatientBirthdate(){
  for (let row of rows) {
    var res = row.lastElementChild.innerHTML.replace(/\d{4}-\d{2}-\d{2}/g, replacer)
    console.log(res)
    row.lastElementChild.innerHTML = res;
  }
  function replacer(match) {
    var matches = [];
    var newDate;
    match.replace(/\b\w+\b/g, dateHandler)
    function dateHandler(x){
      matches.push(x);
    }
    matches.reverse()
    newDate = matches.join('/');
    return newDate
  }
}
window.addEventListener("load", changePatientBirthdate);

