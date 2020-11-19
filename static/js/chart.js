var ctx = document.getElementsByClassName("chart");

var chartGraph = new Chart(ctx, {
  type: "bar",
  data: {
    labels: [],
    datasets: [{
      label: " Medição",
      backgroundColor: "#6b7adb",
      hoverBackgroundColor: "#96a4ff",
      barThickness: 25,
      data: [],
    }],
  },

  options: {
    legend: {
      display: false
    },
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        gridLines: {
          drawOnChartArea: false
        },
      }],
      yAxes: [{
        gridLines: {
          drawOnChartArea: false,
        },
        ticks: {
          //display: false,
          suggestedMin: 0,
          stepsize: 10,
        }
      }]
    }

  }
});

for (let row of rows) {
  chartGraph.data.datasets[0].data.push(row.lastElementChild.lastChild.data);
  chartGraph.data.labels.push(row.childNodes[3].firstChild.data);
}

chartGraph.update();
