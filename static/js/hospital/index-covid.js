$(function() {
    "use strict";

    $('.sparkbar').sparkline('html', { type: 'bar' });

    // Number of Cases
    $(document).ready(function() {
        var options = {
            chart: {
                height: 350,
                type: 'bar',
            },
            colors: ['#59c4bc', '#637aae', '#868e96'],
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
                name: 'CONFIRMED',
                data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
            }, {
                name: 'RECOVERED',
                data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
            }, {
                name: 'DEATHS',
                data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
            }],
            xaxis: {
                categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            },
            yaxis: {
                title: {
                    text: 'Our Hospital'
                }
            },
            fill: {
                opacity: 1

            },
            tooltip: {
                y: {
                    formatter: function (val) {
                        //return "$ " + val + " thousands"
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

    // Use by Gander
    $(document).ready(function(){
        var chart = c3.generate({
            bindto: '#Use-by-gander', // id of chart wrapper
            data: {
                columns: [
                    // each columns data
                    ['data1', 68],
                    ['data2', 32],
                ],
                type: 'pie', // default type of chart
                colors: {
                    'data1': Amaze.colors["theme-cyan1"],
                    'data2': Amaze.colors["theme-cyan2"],
                },
                names: {
                    // name of each serie
                    'data1': 'MALE',
                    'data2': 'FEMALE',
                }
            },
            axis: {
            },
            legend: {
                show: true, //hide legend
            },
            padding: {
                bottom: 0,
                top: 0
            },
        });
    });


    if( $('#Top-Country').length > 0 ){

        $('#Top-Country').vectorMap(
        {
            map: 'world_mill_en',
            backgroundColor: 'transparent',
            borderColor: '#fff',
            borderOpacity: 0.25,
            borderWidth: 0,
            color: '#e6e6e6',
            regionStyle : {
                initial : {
                fill : '#cccccc'
                }
            },

            markerStyle: {
            initial: {
                    r: 5,
                    'fill': '#fff',
                    'fill-opacity':1,
                    'stroke': '#000',
                    'stroke-width' : 1,
                    'stroke-opacity': 0.4
                },
            },
        
            markers : [{
                latLng : [21.00, 78.00],
                name : 'INDIA : 350'
            
            },
                {
                latLng : [-33.00, 151.00],
                name : 'Australia : 250'
                
            },
                {
                latLng : [36.77, -119.41],
                name : 'USA : 250'
                
            },
                {
                latLng : [55.37, -3.41],
                name : 'UK   : 250'
                
            },
                {
                latLng : [25.20, 55.27],
                name : 'UAE : 250'
            
            }],

            series: {
                regions: [{
                    values: {
                        "US": '#2CA8FF',
                        "SA": '#49c5b6',
                        "AU": '#18ce0f',
                        "IN": '#f96332',
                        "GB": '#FFB236',
                    },
                    attribute: 'fill'
                }]
            },
            hoverOpacity: null,
            normalizeFunction: 'linear',
            zoomOnScroll: false,
            scaleColors: ['#000000', '#000000'],
            selectedColor: '#000000',
            selectedRegions: [],
            enableZoom: false,
            hoverColor: '#fff',
        });
    }
});