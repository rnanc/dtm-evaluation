let ctx = document.getElementsByClassName("chart");
let opts = {
  type: "bar",
  data: {
    labels: [],
    datasets: [
      {
        label: " Medição",
        backgroundColor: "#6b7adb",
        hoverBackgroundColor: "#5366e0",
        fill: true,
        pointRadius: 6,
        pointHoverRadius: 5,
        barThickness: 25,
        data: [],
      },
    ],
  },
  options: {
    legend: {
      display: false,
    },
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      xAxes: [
        {
          gridLines: {
            drawOnChartArea: false,
          },
        },
      ],
      yAxes: [
        {
          gridLines: {
            drawOnChartArea: false,
            //drawTicks: false,
          },
          ticks: {
            //display: false,
            suggestedMin: 0,
            stepsize: 10,
          },
        },
      ],
    },
  },
};

let chartGraph = new Chart(ctx, opts);

for (let row of rows) {
  chartGraph.data.datasets[0].data.push(row.lastElementChild.lastChild.data);
  chartGraph.data.labels.push(row.childNodes[3].firstChild.data);
}

chartGraph.update();

let toggle = false;
function toggleHandler() {
  toggle = !toggle;
  let toggleButton = document.querySelectorAll(".toggleLineChart span");

  if (toggle) {
    toggleButton[0].innerHTML = "bar_chart";

    chartGraph.destroy();

    opts.type = "line";
    opts.data.datasets[0].fill = false;

    chartGraph = new Chart(ctx, opts);

    chartGraph.update();
  } else {
    toggleButton[0].innerHTML = "show_chart";

    chartGraph.destroy();

    opts.type = "bar";
    opts.data.datasets[0].fill = true;

    chartGraph = new Chart(ctx, opts);

    chartGraph.update();
  }
}
