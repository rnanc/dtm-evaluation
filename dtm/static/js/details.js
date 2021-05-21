let rows = document.querySelectorAll('tbody tr');

for (let row of rows) {
  row.addEventListener('click', function () {
      window.location.href = '/exam_data/'+row.id
  });
}

