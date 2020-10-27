let rows = document.querySelectorAll('tbody tr');

for (let row of rows) {
  row.addEventListener('click', function () {
      window.location.href = '/details/'+row.id
  });
}

