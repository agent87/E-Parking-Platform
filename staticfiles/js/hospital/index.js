$(function() {
    "use strict";

    // Total Revenue
    $(document).ready(function() {
        var options = {
            chart: {
                height: 380,
                type: 'line',
                toolbar: {
                    show: false,
                },
            },
            colors: ['#613c95', '#fff133'],
            series: [{
                name: 'Operation',
                type: 'column',
                data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160]
            }, {
                name: 'Pharmacy',
                type: 'line',
                data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16]
            }],
            stroke: {
                width: [0, 4]
            },        
            
            labels: ['01 Aug 2020', '02 Aug 2020', '03 Aug 2020', '04 Aug 2020', '05 Aug 2020', '06 Aug 2020', '07 Aug 2020', '08 Aug 2020', '09 Aug 2020', '10 Aug 2020', '11 Aug 2020', '12 Aug 2020'],
            xaxis: {
                type: 'datetime'
            },
            yaxis: [{
                title: {
                    text: 'Operation',
                },

            }, {
                opposite: true,
                title: {
                    text: 'Pharmacy'
                }
            }]
        }
        var chart = new ApexCharts(
            document.querySelector("#apex-chart-line-column"),
            options
        );

        chart.render();
    });

    // Visitors Statistics
    $(document).ready(function() {

        function generateData(baseval, count, yrange) {
            var i = 0;
            var series = [];
            while (i < count) {
                var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;;
                var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
                var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;

                series.push([x, y, z]);
                baseval += 86400000;
                i++;
            }
            return series;
        }
        var options = {
            chart: {
                height: 350,
                type: 'bubble',
                toolbar: {
                    show: false,
                },
            },
            colors: ['#613c95', '#637aae'],
            dataLabels: {
                enabled: false
            },
            series: [{
                    name: 'Direct',
                    data: generateData(new Date('11 June 2020 GMT').getTime(), 20, {
                        min: 10,
                        max: 60
                    })
                },
                {
                    name: 'Paid',
                    data: generateData(new Date('11 June 2020 GMT').getTime(), 20, {
                        min: 10,
                        max: 60
                    })
                }
            ],
            fill: {
                opacity: 0.8
            },
            xaxis: {
                tickAmount: 10,
                type: 'category',
            },
            yaxis: {
                max: 100
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#apex-simple-bubble"),
            options
        );

        chart.render();
    });
   
});
