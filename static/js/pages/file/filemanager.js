$(document).ready(function() {
    var options = {
        chart: {
            height: 300,
            type: 'bar',
        },
        colors: ['#dd5e89', '#a890d3', '#72c2ff'],
        plotOptions: {
            bar: {
                horizontal: false,
                columnWidth: '55%',
                endingShape: 'rounded'	
            },
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            show: true,
            width: 2,
            colors: ['transparent']
        },
        series: [{
            name: 'Documentsof',
            data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
        }, {
            name: 'Mediaof',
            data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
        }, {
            name: 'Images',
            data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
        }],
        xaxis: {
            categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
        },
        fill: {
            opacity: 1

        },
        tooltip: {
            y: {
                formatter: function (val) {
                    return "$ " + val + " thousands"
                }
            }
        }
    }

    var chart = new ApexCharts(
        document.querySelector("#apex-basic-column"),
        options
    );

    chart.render();
});