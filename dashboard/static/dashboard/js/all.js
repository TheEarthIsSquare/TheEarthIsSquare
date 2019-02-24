$.ajax({
  url: $("#ig-likes-chart").attr("data-url"),
  dataType: 'json',
  success: function (data) {
    Highcharts.chart("ig-likes-chart", data);
  }
});

$.ajax({
  url: $("#ig-followers-chart").attr("data-url"),
  dataType: 'json',
  success: function (data) {
    Highcharts.chart("ig-followers-chart", data);
  }
});
