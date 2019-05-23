$(document).ready(function () {
    new Chartist.Bar('#main-chart', {
      labels: penyakit_labels,
      series: [ penyakit_counts ]
    }, {
      seriesBarDistance: 10,
      axisX: {
        offset: 60
      },
      axisY: {
        offset: 80,
        labelInterpolationFnc: function(value) {
          return value + ' Kasus'
        },
        scaleMinSpace: 100
      }
    });

    new Chartist.Bar('#gejala-chart', {
      labels: gejala_labels,
      series: [ gejala_counts ]
    }, {
      seriesBarDistance: 10,
      axisX: {
        offset: 60,
        labelInterpolationFnc: function(value) {
          return 'G' + value
        }
      },
      axisY: {
        offset: 80,
        labelInterpolationFnc: function(value) {
          return value
        },
        scaleMinSpace: 100
      }
    });
});