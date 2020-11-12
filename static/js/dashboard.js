let rows = document.querySelectorAll('tbody tr');

for (let row of rows) {
  row.addEventListener('click', function () {
      window.location.href = '/details/'+row.id
  });
}

//Função para procurar paciente.
let search_box = document.getElementById("search_box");
function getListPatients(){
  patients_names = []
  patients_tr = []
  for (let row of rows) {
    patients_names.push(row.firstElementChild.firstChild.data.toLowerCase());
    patients_tr.push(row)
  }
  patients_names_filter = []
  patients_names.forEach(element => {
    if (element.indexOf(this.value.toLowerCase()) == 0){
      patients_names_filter.push(element);
    }
  });
  if (this.value == null){
    for (let row of patients_tr) {
      row[i].style = "display: flex;";
    }
  }
  else{
    for (let i in patients_tr) {
      nome_aux = patients_names[i];
      if (patients_names_filter.indexOf(nome_aux) > -1){
        rows[i].style = "display: flex;";
      }
      else{
        rows[i].style = "display: none;";
      }
    }
  }
}
search_box.addEventListener('input', getListPatients);
search_box.addEventListener('change', getListPatients);

